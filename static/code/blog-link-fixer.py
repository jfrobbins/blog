import os
import re
from urllib.parse import urlparse, parse_qs

def find_article_files(root_dir):
    article_dict = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    match = re.search(r'original filename: (\d+)', content)
                    if match:
                        article_id = match.group(1)
                        article_dict[article_id] = file_path
    return article_dict

def update_links(root_dir, article_dict):
    link_pattern = re.compile(r'\[([^]]+)\]\((http://jrobb\.org/blog/index\.php\?article=(\d+))\)')
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r+', encoding='utf-8') as file:
                    content = file.read()
                    new_content = link_pattern.sub(lambda m: update_link(m, article_dict), content)
                    file.seek(0)
                    file.write(new_content)
                    file.truncate()

def update_link(match, article_dict):
    title, old_url, article_id = match.groups()
    if article_id in article_dict:
        new_path = article_dict[article_id].replace(root_dir, '').lstrip('/')
        return f'[{title}]({{< ref "{new_path}" >}})'
    return match.group(0)  # If not found, return the original link

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fix blog post URLs in markdown files.")
    parser.add_argument('-i', '--input', required=True, help="Root directory of the blog content")
    args = parser.parse_args()
    
    article_dict = find_article_files(args.input)
    update_links(args.input, article_dict)
    print("URLs have been updated in the markdown files.")
