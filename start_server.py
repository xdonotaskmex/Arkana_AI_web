import os
import sys
import subprocess

# Change to the correct directory (root directory where index.html is located)
os.chdir(r"c:\Users\user\OneDrive\Dokumenty\GitHub\Arkana_AI_web")

# Verify that index.html exists in this directory
if not os.path.exists("index.html"):
    print("ERROR: index.html not found in the current directory")
    print("Current directory:", os.getcwd())
    print("Files in directory:", os.listdir("."))
    sys.exit(1)

# Start the server
print("Starting local development server...")
print("Serving from directory:", os.getcwd())
print("Access your site at: http://localhost:8000")
print("For production deployment, ensure all resources use HTTPS protocol")
subprocess.run([sys.executable, "-m", "http.server", "8000"])