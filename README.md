# 🚀 LinkedInPostMaster

AI-powered Streamlit application for optimizing LinkedIn posts based on 74 high-performing reference posts with optional o3-judge evaluation.

## Features

- Drei Optimierungsvarianten pro Modell (emotional, storytelling, lokal) ohne Emojis und mit Erhalt aller Links.
- Unterstützte Modelle: `gpt-4o`, `gpt-4.1`, `gpt-5` (via `responses.create`).
- Parallelmodus zur gleichzeitigen Ausführung aller Modelle.
- Optionale Richter:innenfunktion (`o3`), die auf Basis von Post-Beispielen den besten Vorschlag auswählt.
- Regelbasierte Voranalyse, die identifizierte Stärken und Schwächen hervorhebt.
- Scrollbare, farbkodierte Ergebnisblöcke für verbesserte Lesbarkeit.
- Manuelle Eingabe des OpenAI-API-Schlüssels im UI, falls keine `.env` vorhanden ist.

## Projektstruktur

```
LinkedInPostMaster/
├── app.py                      # Streamlit-Einstiegspunkt
├── README.md                   # Project docs
├── requirements.txt            # Minimale Abhängigkeiten (Streamlit, OpenAI, dotenv)
├── posts.json                  # Historische Beispielposts (Quelle für Regeln/Prompts)
└── src/
    ├── __init__.py
    ├── analysis/
    │   ├── __init__.py
    │   └── post_analysis.py    # Regelbasierte Analyse
    ├── config.py               # AppConfig (Modelle, Defaults)
    ├── data/
    │   ├── __init__.py
    │   └── post_examples.py    # High-/Medium-/Low-Performer Beispiele
    ├── domain/
    │   ├── __init__.py
    │   └── performance_rules.py# Performanceregeln
    ├── prompts/
    │   ├── __init__.py
    │   └── optimizer_prompt.py # Prompt-Erzeugung für Optimierer
    ├── services/
    │   ├── __init__.py
    │   ├── judge_service.py    # o3-Judge
    │   └── llm_client.py       # OpenAI-Client & Parsing
    └── ui/
        ├── __init__.py
        └── components.py       # Streamlit-UI-Komponenten (Panels & Judge-Output)
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### OpenAI API Key

**Lokal (empfohlen):**

1. Kopiere `.env.example` zu `.env`:
   ```bash
   cp .env.example .env
   ```

2. Füge deinen API Key ein:
   ```bash
   OPENAI_API_KEY=sk-your-actual-api-key
   ```

**Alternative:** Manuell im rechten Seitenmenü der App eingeben.

## App starten

```bash
streamlit run app.py
```

Die App öffnet sich im Browser (Standard: http://localhost:8501).

## Deployment

### Streamlit Cloud (Empfohlen)

Siehe **[DEPLOYMENT.md](DEPLOYMENT.md)** für detaillierte Schritt-für-Schritt Anleitung.

**Quick Start:**
```bash
# 1. Code auf GitHub pushen
git add .
git commit -m "Initial deployment"
git push origin master

# 2. Streamlit Cloud öffnen
# → share.streamlit.io
# → New app → Repository auswählen
# → Secrets konfigurieren: OPENAI_API_KEY
# → Deploy!
```

**Wichtig:**
- ✅ `.env` wird NICHT committed (in `.gitignore`)
- ✅ API Key über Streamlit Secrets konfigurieren
- ✅ Automatisches Re-Deployment bei jedem Git Push

## Tests / Validierung

Das Projekt enthält automatisierte Unit-Tests für die Kernfunktionalitäten.

### Tests ausführen

```bash
# Alle Tests ausführen
./test_run.sh

# Mit ausführlicher Ausgabe
./test_run.sh --verbose

# Mit Coverage-Report
./test_run.sh --coverage

# Spezifischen Test ausführen
./test_run.sh --specific test_llm_client.py
```

### Test-Struktur

```
tests/
├── test_llm_client.py          # Tests für OpenAI Client & Response Parsing
├── test_optimizer_prompt.py    # Tests für Prompt-Generierung
└── test_post_analysis.py       # Tests für regelbasierte Analyse
```

### Manuelle Validierung

- Vor Deployments: Smoke-Test lokal durchführen (`streamlit run app.py`)
- API-Integration: Testen mit realem OpenAI API Key

## Bekannte Limitierungen

- Historische Datenbasis: nur 74 Posts → eingeschränkte Repräsentativität.
- o3-Judge kann nur mit passenden API-Limits verwendet werden.
- Es werden keine Kostenkontrollen für parallele API-Aufrufe vorgenommen.

## Weiterentwicklungsideen

- ✅ ~~Unit-Tests für Analyse- und Prompt-Logik~~ (implementiert)
- Integration-Tests für End-to-End-Workflows
- Konfigurierbare Regeln (z.B. via YAML/JSON im Backend)
- Persistenzschicht für Nutzer:innenprofile oder gespeicherte Optimierungen
- Kostenmonitoring bei intensiven LLM-Abfragen
- CI/CD Pipeline mit automatischen Tests

## Lizenz

Nicht angegeben. Bitte bei Bedarf ergänzen.


