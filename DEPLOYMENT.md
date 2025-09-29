# Deployment Guide - LinkedInPostMaster

## 🚀 Streamlit Cloud Deployment

### Vorbereitung

1. **GitHub Repository vorbereiten**
   ```bash
   git add .
   git commit -m "Prepare for deployment: Add configs and tests"
   git push origin master
   ```

2. **Streamlit Cloud Account**
   - Gehe zu [share.streamlit.io](https://share.streamlit.io)
   - Melde dich mit deinem GitHub Account an
   - Autorisiere Streamlit für deine Repositories

### Deployment Schritte

1. **New App erstellen**
   - Klicke auf "New app" in Streamlit Cloud
   - Wähle dein Repository: `LinkedInPostMaster`
   - Branch: `master`
   - Main file path: `app.py`

2. **Umgebungsvariablen konfigurieren**
   
   In den Advanced Settings → Secrets füge hinzu:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```

3. **Python Version** (optional)
   - Streamlit Cloud erkennt automatisch `.python-version` (3.11)
   - Falls nötig: In Advanced Settings Python 3.11 auswählen

4. **Deploy!**
   - Klicke auf "Deploy"
   - Warte auf Build-Prozess (~2-3 Minuten)
   - App wird unter `https://[username]-linkedin.streamlit.app` verfügbar sein

### Nach dem Deployment

#### Monitoring
- Prüfe Logs in Streamlit Cloud Dashboard
- Teste alle Features mit echtem OpenAI API Key
- Überwache API Usage in OpenAI Dashboard

#### Updates deployen
```bash
# Änderungen committen
git add .
git commit -m "Update: [Beschreibung]"
git push origin master

# Streamlit Cloud deployed automatisch bei jedem Push!
```

#### Troubleshooting

**Problem: "ModuleNotFoundError"**
- Lösung: Prüfe ob alle Dependencies in `requirements.txt` sind
- Prüfe ob Python Version kompatibel ist

**Problem: "OpenAI API Error"**
- Lösung: Prüfe ob `OPENAI_API_KEY` in Secrets konfiguriert ist
- Teste API Key lokal zuerst

**Problem: App lädt langsam**
- Lösung: Streamlit Cloud hat manchmal Cold Starts
- Erwäge Caching für häufige Operationen

## 📋 Pre-Deployment Checklist

- [x] `.gitignore` konfiguriert und `.env` nicht committed
- [x] `.env.example` als Template vorhanden
- [x] `requirements.txt` mit spezifischen Versionen
- [x] `.streamlit/config.toml` für UI-Konfiguration
- [x] `.python-version` für Python 3.11
- [x] Tests funktionieren (`./test_run.sh`)
- [x] README.md dokumentiert
- [x] GitHub Actions für CI/CD (optional)

## 🔐 Sicherheit

### API Keys
- ❌ **NIEMALS** API Keys in Code committen
- ✅ Nutze Streamlit Secrets in Cloud
- ✅ Nutze `.env` lokal (in `.gitignore`)

### Best Practices
- Verwende Environment Variables für alle Secrets
- Implementiere Rate Limiting für API Calls
- Überwache API Costs in OpenAI Dashboard
- Beschränke Zugriff auf App falls nötig (Streamlit Cloud Pro Feature)

## 🔄 CI/CD Pipeline

GitHub Actions läuft automatisch bei jedem Push:
- ✅ Tests ausführen
- ✅ Code Formatting prüfen (black)
- ✅ Dependencies installieren

Siehe: `.github/workflows/tests.yml`

## 📊 Monitoring & Maintenance

### Performance
- Überwache Response Times in Streamlit Cloud
- Optimiere API Calls (Batch Requests)
- Nutze `st.cache_data` für statische Daten

### Kosten
- OpenAI API Costs: Überwache Usage Dashboard
- Streamlit Cloud: Kostenlos für Public Apps
- Erwäge Rate Limits für Production

## 🆘 Support

Bei Problemen:
1. Prüfe Streamlit Cloud Logs
2. Teste lokal mit `streamlit run app.py`
3. Prüfe GitHub Issues
4. Streamlit Community Forum: [discuss.streamlit.io](https://discuss.streamlit.io)
