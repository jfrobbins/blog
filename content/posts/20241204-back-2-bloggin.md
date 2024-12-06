+++
title = '20241204 Back 2 Bloggin'
date = 2024-12-06T07:31:31-05:00
draft = true
+++

Well, I've resurrected this blog for better or worse. 
In the past, this blog has been many things over the years -- Octopress/Pelican/Jekyl/JBS, and before that Wordpress, and before that another homegrown system.

I'm actually not too sure how much content has come through, but it seems pretty old.  Also I've realized that 1) my posts have not been great, and 2) I didn't do the best job over the years of keeping things formatted.

Lately I was wondering if I still owned my domains, and I still have `jrobb.org` for another year -- so I figured I'd give it another go. 
It's nice to have somewhere to post random things, and it has never been easier since Github Pages makes it way too easy with a static site generator like hugo.

So the first thing I did was look back at my old content, which I had preserved in a github repo -- more accurately, a series of repos from the format changes over the years.
Now, to convert the posts over to [Hugo's](https://gohugo.io/) format.

While I've had and used [ChatGPT](https://chatgpt.com/) for a lot of things over the past couple of years, I wanted to try out [Grok](https://grok.x.com).
It was perfect timing when I came across a Thanksgiving discount that made the [X Premium](https://help.x.com/en/using-x/x-premium) subscription <$6/month. 
I snagged it and cancelled my $20/month ChatGPT subscription.


So I asked Grok to create a python script to convert the posts -- bing, bang, boom, [here's](https://gist.github.com/jfrobbins/f495c18190801b3532707a0abdc2cf26) what I ended up with.
It mostly worked, but I definitely noticed that it's not perfect and also there are a lot of weird artifacts from transitioning from all of the different blog formats over the years.
But here we are -- the content mostly converted over and now is up.  

It is pretty hilarious for me to read about what I was doing so many years ago as I stopped updating around 2013/2014 -- 
then I divorced in 2016 which through my world into a blender and I lost a lot of my servers and backups in the chaos.

So now I'm trying to spin things back up, and be better about documenting anything that I do.
As another _main_ goal, I want to document more things for my kids, so they can have some source of information from my even when I'm gone.

Hopefully I'm better about doing that, and can stick to it this time!



## convert-pelican-posts-to-hugo-md.py

I linked to the conversion script github gist above, but I'll paste the source here as well -- we never know what sites will be around in another 10 years.

```
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

    
"""
convert-pelican-posts-to-hugo-md.py

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
```
