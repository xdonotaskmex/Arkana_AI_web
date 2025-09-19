#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import codecs

def has_bom(file_path):
    """Check if a file has BOM"""
    with open(file_path, 'rb') as f:
        raw = f.read(4)
    for enc, boms in \
            ('utf-8-sig', (codecs.BOM_UTF8,)), \
            ('utf-16', (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)), \
            ('utf-32', (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
        if any(raw.startswith(bom) for bom in boms):
            return enc
    return None

def remove_bom(file_path):
    """Remove BOM from a file"""
    # Read the file
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # Check for BOM and remove if present
    if content.startswith(codecs.BOM_UTF8):
        content = content[len(codecs.BOM_UTF8):]
        print(f"Removed UTF-8 BOM from {file_path}")
    elif content.startswith(codecs.BOM_UTF16_LE):
        content = content[len(codecs.BOM_UTF16_LE):]
        print(f"Removed UTF-16 LE BOM from {file_path}")
    elif content.startswith(codecs.BOM_UTF16_BE):
        content = content[len(codecs.BOM_UTF16_BE):]
        print(f"Removed UTF-16 BE BOM from {file_path}")
    elif content.startswith(codecs.BOM_UTF32_LE):
        content = content[len(codecs.BOM_UTF32_LE):]
        print(f"Removed UTF-32 LE BOM from {file_path}")
    elif content.startswith(codecs.BOM_UTF32_BE):
        content = content[len(codecs.BOM_UTF32_BE):]
        print(f"Removed UTF-32 BE BOM from {file_path}")
    
    # Write back without BOM
    with open(file_path, 'wb') as f:
        f.write(content)

def main():
    # Files to check
    files_to_check = [
        'arkana-ai-web/index.html',
        'arkana-ai-web/styles.css',
        'arkana-ai-web/script.js',
        'arkana-ai-web/404.html',
        'index.html'
    ]
    
    # Check each file
    for file_name in files_to_check:
        if os.path.exists(file_name):
            bom_type = has_bom(file_name)
            if bom_type:
                print(f"Found {bom_type} BOM in {file_name}")
                remove_bom(file_name)
            else:
                print(f"No BOM found in {file_name}")

if __name__ == "__main__":
    main()