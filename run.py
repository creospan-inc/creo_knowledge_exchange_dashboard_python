#!/usr/bin/env python
"""
Run script for the AI Metrics Dashboard
Simply execute this file to start the dashboard:
python run.py
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import and run the main function
from app.main import main

if __name__ == "__main__":
    main() 