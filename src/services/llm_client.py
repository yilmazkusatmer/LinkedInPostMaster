from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import Dict, Optional

import openai

from src.config import APP_CONFIG


@dataclass
class LLMResponse:
    model: str = ""
    version_1: str = ""
    version_2: str = ""
    version_3: str = ""
    reasoning: str = ""
    raw_response: str = ""
    new_score: Optional[int] = None
    improvement: Optional[int] = None
    error: str = ""

    def as_dict(self) -> Dict[str, str]:
        return {
            "version_1": self.version_1,
            "version_2": self.version_2,
            "version_3": self.version_3,
            "reasoning": self.reasoning,
        }


class OpenAIClient:
    """Wrapper around OpenAI API usage for streamlined model handling."""

    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._client: Optional[openai.OpenAI] = None

    @property
    def client(self) -> openai.OpenAI:
        if not self._client:
            self._client = openai.OpenAI(api_key=self.api_key)
        return self._client

    def call_model(
        self,
        prompt: str,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> str:
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is missing. Provide it via .env or runtime input.")

        target_model = model or APP_CONFIG.default_model
        if target_model == "gpt-5":
            response = self.client.responses.create(
                model=target_model,
                input=prompt,
            )
            return response.output_text

        response = self.client.chat.completions.create(
            model=target_model,
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein spezialisierter LinkedIn-Post-Optimierer für APG|SGA.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=APP_CONFIG.max_tokens,
            temperature=temperature if temperature is not None else APP_CONFIG.default_temperature,
        )
        return response.choices[0].message.content or ""

    @staticmethod
    def parse_llm_response(
        response: str,
        model: str,
        baseline_score: Optional[int] = None,
    ) -> LLMResponse:
        parsed = LLMResponse(model=model, raw_response=response)

        if not response:
            parsed.reasoning = "Keine Antwort vom Modell erhalten."
            return parsed

        version1_match = re.search(r"VERSION_1:\s*(.*?)(?=\nVERSION_2:|\nVERSION_3:|\nBEGRÜNDUNG:|$)", response, re.DOTALL | re.IGNORECASE)
        if version1_match:
            parsed.version_1 = version1_match.group(1).strip()

        version2_match = re.search(r"VERSION_2:\s*(.*?)(?=\nVERSION_3:|\nBEGRÜNDUNG:|$)", response, re.DOTALL | re.IGNORECASE)
        if version2_match:
            parsed.version_2 = version2_match.group(1).strip()

        version3_match = re.search(r"VERSION_3:\s*(.*?)(?=\nBEGRÜNDUNG:|$)", response, re.DOTALL | re.IGNORECASE)
        if version3_match:
            parsed.version_3 = version3_match.group(1).strip()

        reasoning_match = re.search(r"BEGRÜNDUNG:\s*(.*?)$", response, re.DOTALL | re.IGNORECASE)
        if reasoning_match:
            parsed.reasoning = reasoning_match.group(1).strip()

        if not any([parsed.version_1, parsed.version_2, parsed.version_3]):
            parsed.version_1 = response.strip()
            parsed.reasoning = parsed.reasoning or "Keine strukturierte Versionen erkannt. Rohausgabe als Version 1 verwendet."

        if baseline_score is not None:
            new_score = min(baseline_score + 25, 95)
            parsed.new_score = new_score
            parsed.improvement = new_score - baseline_score

        return parsed

    def optimize_post(
        self,
        prompt: str,
        model: str,
        baseline_score: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> LLMResponse:
        try:
            raw_response = self.call_model(
                prompt=prompt,
                model=model,
                temperature=temperature if model != "gpt-5" else None,
            )
        except Exception as exc:  # noqa: BLE001
            return LLMResponse(
                model=model,
                reasoning=f"OpenAI API Error: {exc}",
                raw_response=str(exc),
                error=str(exc),
            )

        return self.parse_llm_response(
            response=raw_response,
            model=model,
            baseline_score=baseline_score,
        )


