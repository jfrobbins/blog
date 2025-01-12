"""
Usage:
    python3 generate-file-list.py -i <input_directory> [-m] [-o <output_file>]

Examples:
    - To generate an HTML file tree from 'audio/' directory:
      python3 generate-file-list.py -i audio/
    
    - To generate a Markdown file tree from 'audio/' directory:
      python3 generate-file-list.py -i audio/ -m
    
    - To specify both input and output for HTML:
      python3 generate-file-list.py -i custom_audio_dir/ -o custom_index.html
    
    - To specify both input and output for Markdown:
      python3 generate-file-list.py -i custom_audio_dir/ -m -o content/custom_audio/_index.md

Arguments:
    -i, --input     : Specify the input directory. Defaults to 'audio/'.
    -o, --output    : Specify the output file path. If not provided, defaults to 
                      'index.html' in the input directory for HTML output or 
                      'content/audio/_index.md' for Markdown output.
    -m, --markdown  : Use this flag to output in Markdown format instead of HTML.
    -r, --recursive : This flag is on by default for recursive traversal. 
                      It's included for consistency but not necessary to specify.

Note:
    - Ensure your Hugo site configuration supports the directory structure 
      where Markdown files are placed for correct URL paths.
"""

import os
import argparse

def generate_file_tree(input_dir, output_file, recursive=True, markdown=False):
    if markdown:
        with open(output_file, 'w') as f:
            f.write("# Audio Files\n\n")
            for root, dirs, files in os.walk(input_dir):
                # Sort directories and files alphabetically
                dirs.sort()
                files.sort()
                
                relative_root = os.path.relpath(root, input_dir).replace('\\', '/')
                full_path = os.path.join('audio', relative_root).replace('\\', '/')
                
                if relative_root == '.':
                    f.write(f"## audio/\n")  # Corrected title for root directory
                    if files:
                        f.write("\n")
                else:
                    # Only write headers for directories with files or subdirectories
                    if files or dirs:
                        f.write(f"### {full_path}/\n\n")
                
                # List files in the current directory
                for file in files:
                    if file.endswith(('.mp3', '.wav', '.ogg')):  # Adjust extensions as needed
                        # Correct the path to avoid duplicate 'audio' and remove './'
                        file_path = os.path.join(relative_root, file).replace('\\', '/').replace('./', '')
                        f.write(f"- [{file}](/audio/{file_path})\n")
                
                # Add a newline after listing files if there are more directories or files to come
                if files and (dirs or next(os.walk(root))[1] or next(os.walk(root))[2]):
                    f.write("\n")
    else:
        with open(output_file, 'w') as f:
            f.write('<ul>\n')
            for root, dirs, files in os.walk(input_dir):
                # Sort directories and files alphabetically
                dirs.sort()
                files.sort()
                
                relative_root = os.path.relpath(root, input_dir).replace('\\', '/')
                full_path = os.path.join('audio', relative_root).replace('\\', '/')
                
                if relative_root == '.':
                    f.write(f'<li><b>{full_path}/</b></li>\n')
                else:
                    # Write directory link with full path
                    f.write(f'<li><a href="/{full_path}/">{full_path}/</a></li>\n')
                    f.write('<ul>\n')
                
                # List files in the current directory
                for file in files:
                    if file.endswith(('.mp3', '.wav', '.ogg')):  # Adjust extensions as needed
                        file_path = os.path.join(full_path, file)
                        f.write(f'<li><a href="/{file_path}">{file}</a></li>\n')
                
                # Close the nested <ul> for directories if it's not the root
                if relative_root != '.':
                    f.write('</ul>\n')
            f.write('</ul>\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a file tree for static site.")
    parser.add_argument('-i', '--input', default='audio/', help='Input directory')
    parser.add_argument('-o', '--output', default=None, help='Output file path')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursive directory traversal', default=True)
    parser.add_argument('-m', '--markdown', action='store_true', help='Output in Markdown format')
    
    args = parser.parse_args()
    
    # Ensure the input directory exists
    if not os.path.isdir(args.input):
        raise ValueError(f"Input directory '{args.input}' does not exist.")
    
    # Determine the output file path
    if args.markdown:
        if args.output is None:
            # Default path for Markdown output
            content_path = 'content/audio/'
            os.makedirs(content_path, exist_ok=True)
            output_file = os.path.join(content_path, '_index.md')
        else:
            output_file = args.output
    else:
        if args.output is None:
            output_file = os.path.join(args.input, 'index.html')
        else:
            output_file = args.output
            # Ensure the output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    generate_file_tree(args.input, output_file, args.recursive, args.markdown)
    print(f"File tree generated and saved to {output_file}")

"""
THE UNLICENSE

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

For more information, please refer to <http://unlicense.org/>
"""
