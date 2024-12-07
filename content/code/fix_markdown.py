import os
import argparse
import re

def fix_markdown_links(text):
    # Fix broken link format
    text = re.sub(r'("  target="blank)', '', text)
    
    # Convert HTML links to Markdown format
    text = re.sub(r'<a href="([^"]+)"[^>]*>([^<]+)</a>', r'[\2](\1)', text)
    
    return text

def process_files(start_path):
    for root, _, files in os.walk(start_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Apply fixes to the content
                modified_content = fix_markdown_links(content)
                
                # Write back the modified content if there were changes
                if content != modified_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(modified_content)
                    print(f"Modified file: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Fix Markdown links in files.")
    parser.add_argument('start_path', help='The directory to start from')
    args = parser.parse_args()
    
    if not os.path.isdir(args.start_path):
        print(f"Error: {args.start_path} is not a valid directory.")
        return
    
    process_files(args.start_path)
    print("Processing completed.")

if __name__ == "__main__":
    main()

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
