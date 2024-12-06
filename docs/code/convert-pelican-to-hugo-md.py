import os
import yaml
import argparse
from datetime import datetime

def convert_post(input_path, output_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    # Initialize front matter with default values
    front_matter = {
        'draft': False,
        'date': None,
        'modified': None,
        'title': None,
        'category': None,
        'tags': [],
        'slug': None,
        'authors': None
    }
    
    # Process each line of the file
    content = []
    in_frontmatter = True
    for line in lines:
        if in_frontmatter:
            if line.strip() == "":
                in_frontmatter = False  # End of front matter
            else:
                key, value = line.strip().split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                if key in ['date', 'modified']:
                    try:
                        dt = datetime.strptime(value, "%Y-%m-%d")
                        front_matter[key] = dt.isoformat()
                    except ValueError:
                        print(f"Could not parse date '{value}' in file {input_path}. Using original format.")
                        front_matter[key] = value
                elif key == 'tags':
                    front_matter[key] = [item.strip() for item in value.split(',')]
                else:
                    front_matter[key] = value
        else:
            content.append(line)
    
    # Ensure the output directory structure exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    # Write the new file
    with open(output_path, 'w') as file:
        file.write("---\n")
        yaml.dump(front_matter, file, default_flow_style=False, allow_unicode=True)
        file.write("---\n")
        file.writelines(content)

def main():
    parser = argparse.ArgumentParser(description="Convert Pelican posts to Hugo format.")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input directory containing Pelican posts')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output directory for converted posts')
    args = parser.parse_args()

    for root, _, files in os.walk(args.input):
        for file in files:
            if file.endswith('.md'):
                input_path = os.path.join(root, file)
                # Construct the output path relative to the input directory
                relative_path = os.path.relpath(input_path, args.input)
                output_path = os.path.join(args.output, relative_path)
                convert_post(input_path, output_path)

    print("Conversion complete!")

if __name__ == "__main__":
    main()
