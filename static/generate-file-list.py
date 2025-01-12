import os
import argparse

def generate_file_tree(input_dir, output_file, recursive=True):
    with open(output_file, 'w') as f:
        f.write('<ul>\n')
        for root, dirs, files in os.walk(input_dir):
            # Sort directories and files alphabetically
            dirs.sort()
            files.sort()
            
            relative_root = os.path.relpath(root, input_dir).replace('\\', '/')
            
            # Determine the full path from the site root
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
    
    args = parser.parse_args()
    
    # Ensure the input directory exists
    if not os.path.isdir(args.input):
        raise ValueError(f"Input directory '{args.input}' does not exist.")
    
    # Set default output if not provided
    if args.output is None:
        args.output = os.path.join(args.input, 'index.html')
    else:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
    
    generate_file_tree(args.input, args.output, args.recursive)
    print(f"File tree generated and saved to {args.output}")
