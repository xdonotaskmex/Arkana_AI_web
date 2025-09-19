import os
import sys
import subprocess

# Change to the correct directory
os.chdir(r"c:\Users\user\OneDrive\Dokumenty\GitHub\Arkana_AI_web\arkana-ai-web")

# Start the server
print("Starting local development server...")
print("Access your site at: http://localhost:8000")
print("For production deployment, ensure all resources use HTTPS protocol")
subprocess.run([sys.executable, "-m", "http.server", "8000"])
