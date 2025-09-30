#!/bin/bash

# LinkedInPostMaster - Start Script
# Stops any running Streamlit instance and starts fresh

echo "🔍 Checking for running Streamlit processes..."

# Find and kill any running streamlit processes on port 8501
PORT=8501
PID=$(lsof -ti:$PORT)

if [ ! -z "$PID" ]; then
    echo "⚠️  Found Streamlit running on port $PORT (PID: $PID)"
    echo "🛑 Stopping old process..."
    kill -9 $PID
    sleep 1
    echo "✅ Old process stopped"
else
    echo "✅ No running processes found on port $PORT"
fi

# Activate virtual environment and start Streamlit
echo "🚀 Starting LinkedInPostMaster..."
echo ""

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "💡 Run: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
    exit 1
fi

# Start Streamlit using venv
.venv/bin/streamlit run app.py

# Alternative: If you want to activate venv first
# source .venv/bin/activate
# streamlit run app.py

