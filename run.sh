#!/bin/bash
# The Holiday Tree - Startup Script

echo "🎄 Starting The Holiday Tree..."
echo "   Server will be available at http://localhost:8000"
echo ""

# Activate virtual environment and run the FastAPI server
source venv/bin/activate
python main.py
