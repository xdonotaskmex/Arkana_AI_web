#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def normalize_line_endings(file_path):
    """Normalize line endings to LF (\n)"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace CRLF with LF
        content = content.replace('\r\n', '\n')
        # Replace CR with LF (old Mac format)
        content = content.replace('\r', '\n')
        
        # Write back with LF line endings
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        
        print(f"Normalized line endings for {file_path}")
        return True
    except Exception as e:
        print(f"Error normalizing {file_path}: {e}")
        return False

def main():
    # Files to normalize
    files_to_normalize = [
        'arkana-ai-web/index.html',
        'arkana-ai-web/styles.css',
        'arkana-ai-web/script.js',
        'arkana-ai-web/404.html',
        'index.html',
        'CNAME'
    ]
    
    # Normalize each file
    for file_name in files_to_normalize:
        if os.path.exists(file_name):
            normalize_line_endings(file_name)

if __name__ == "__main__":
    main()