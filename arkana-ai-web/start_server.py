import os
import sys
import subprocess

# Change to the correct directory
os.chdir(r"c:\Users\user\OneDrive\Dokumenty\GitHub\Arkana_AI_web\arkana-ai-web")

# Start the server
subprocess.run([sys.executable, "-m", "http.server", "8000"])