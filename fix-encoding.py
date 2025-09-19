#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

def fix_file_encoding(file_path):
    """Fix file encoding and line endings"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Write it back with proper line endings
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        
        print(f"Fixed encoding for {file_path}")
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def main():
    # Files to fix
    files_to_fix = [
        'index.html',
        'styles.css',
        'script.js',
        '404.html'
    ]
    
    # Change to the arkana-ai-web directory
    os.chdir('arkana-ai-web')
    
    # Fix each file
    for file_name in files_to_fix:
        if os.path.exists(file_name):
            fix_file_encoding(file_name)
        else:
            print(f"File not found: {file_name}")

if __name__ == "__main__":
    main()