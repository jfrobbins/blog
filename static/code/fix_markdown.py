import os
import argparse
import re
from pathlib import Path

def fix_markdown_links(text):
    # Fix broken link format
    text = re.sub(r'\s*"?\s*target\s*=\s*"?\s*blank"?\s*', '', text, flags=re.IGNORECASE)
    
    # Convert HTML links to Markdown format
    text = re.sub(r'<a\s+href="([^"]+)"[^>]*>([^<]+)</a>', r'[\2](\1)', text, flags=re.IGNORECASE)
    
    return text

def process_files(start_path):
    files_processed = 0
    files_changed = 0
    for root, _, files in os.walk(start_path):
        for file in files:
            if file.endswith('.md'):
                files_processed += 1
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Apply fixes to the content
                modified_content = fix_markdown_links(content)
                
                print(f"Changed {files_changed} out of {files_processed} files")
                
                # Write back the modified content if there were changes
                if content != modified_content:
                    files_changed += 1
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(modified_content)
                    print(f"Modified file: {file_path}")

    return files_processed, files_changed

def main():
    parser = argparse.ArgumentParser(description="Fix Markdown links in files.")
    parser.add_argument('start_path', type=Path, help='The directory to start from (can be relative or absolute)')
    args = parser.parse_args()
    
    # Convert to absolute path for clarity in error messages
    start_path = args.start_path.expanduser().resolve()
    
    if not start_path.is_dir():
        print(f"Error: {args.start_path} does not exist or is not a directory.")
        return
    
    files_processed, files_changed = process_files(str(start_path))
    print(f"Total files processed: {files_processed}")
    print(f"Total files changed: {files_changed}")
    print("Processing completed.")

if __name__ == "__main__":
    main()


"""
# Unlicense Statement

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
"""
