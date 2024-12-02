import os
import re
import yaml

def convert_to_hugo(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)

                # Create the directory structure in the output directory
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                with open(input_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                
                # Split the content into frontmatter and body
                frontmatter, body = content.split('---', 2)[1:]

                # Parse YAML frontmatter
                try:
                    frontmatter_data = yaml.safe_load(frontmatter)
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML in {input_path}: {e}")
                    continue

                # Convert Pelican's category to Hugo's section if needed
                if 'category' in frontmatter_data:
                    frontmatter_data['section'] = frontmatter_data.pop('category')

                # Adjust date format if needed (Hugo expects YYYY-MM-DD)
                if 'date' in frontmatter_data:
                    date = frontmatter_data['date']
                    if not isinstance(date, str) or not re.match(r'\d{4}-\d{2}-\d{2}', date):
                        # Assuming date is in datetime format, convert to string
                        frontmatter_data['date'] = date.strftime('%Y-%m-%d')

                # Add any Hugo specific fields if required
                # For example, Hugo uses 'tags' instead of 'tags', but this is already in YAML format
                # If you need to add any Hugo-specific fields, add them here

                # Reconstruct the frontmatter in Hugo format
                hugo_frontmatter = '+++\n'
                for key, value in frontmatter_data.items():
                    hugo_frontmatter += f"{key} = \"{value}\"\n"
                hugo_frontmatter += "+++\n\n"

                # Write the new file
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(hugo_frontmatter + body)

                print(f"Converted: {input_path} -> {output_path}")

if __name__ == "__main__":
    input_directory = "path/to/your/pelican/content"  # Change this to your Pelican content directory
    output_directory = "path/to/your/hugo/content"   # Change this to where you want Hugo content to go
    convert_to_hugo(input_directory, output_directory)
