import os
import sys
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Change to the correct directory (root directory where index.html is located)
root_dir = r"c:\Users\user\OneDrive\Dokumenty\GitHub\Arkana_AI_web"
os.chdir(root_dir)

# Verify that index.html exists in this directory
if not os.path.exists("index.html"):
    print("ERROR: index.html not found in the current directory")
    print("Current directory:", os.getcwd())
    print("Files in directory:", os.listdir("."))
    sys.exit(1)

print("Starting local development server...")
print("Serving files from directory:", os.getcwd())
print("Access your site at: http://localhost:8000")
print("For production deployment, ensure all resources use HTTPS protocol")

# Start the server
subprocess.run([sys.executable, "-m", "http.server", "8000"])