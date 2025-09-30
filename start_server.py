import os
import sys
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Custom handler with security headers
class SecureHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        # Add CSP header for basic protection
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://www.googletagmanager.com https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; img-src 'self' data: https:; font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net; connect-src 'self' https://www.googletagmanager.com;")
        super().end_headers()

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

# Start the server with our custom handler
server = HTTPServer(("", 8000), SecureHTTPRequestHandler)
server.serve_forever()