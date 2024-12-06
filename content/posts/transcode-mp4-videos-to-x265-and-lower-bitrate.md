+++
title = 'Transcode Mp4 Videos to X265 and Lower Bitrate'
date = 2024-12-06T08:34:57-05:00
draft = false
+++

Yesterday at work I needed to send some video files, however they were _huge_. 
I used ffmpeg to transcode the files to H.265 and lowered the bitrate until they were an acceptable size -- 
I did this manually on the CLI a few times, and since there were several files in the directory I quickly tired of that.

So of course I needed a script to walk through the dir and do this for me!
I used ChatGPT to create the script once I had the commands how I wanted them. :-)
- [here](https://chatgpt.com/share/6752fc65-1f94-8009-9c93-755aa0bf5407) is a link to the prompts I used to create the source file.

Here is my github gist with documentation, source, etc:
- https://gist.github.com/jfrobbins/0f8ef94b1a7ff780f74a320a2fd9530c

As I tried different CRF values to change the bitrate, the filesize changed drastically.
From the gist above, here's a table showing some example changes based on CRF values:

## CRF value vs filesize
| CRF | Filesize |
| --- | ----- |
| -   | 482.6 MB |
| 30  |  56.5 MB |
| 35  |  21.3 MB |
| 40  |   9.5 MB |

## other useful info:

> Using the H.265 codec, we can compress the video more for the same quality (vs H.264), or gives higher quality for the same size. 
> 
> Push the compression lever further by **increasing** the CRF value — a reasonable range for H.265 may be `24` to `30`.   
> 
> Even **higher CRF values will reduce filesize further**, but sacrifices quality (depending on the video and goals).
> 
> Note that **lower CRF values correspond to higher bitrates**, and hence produce higher quality videos.

# python script

And lastly, here is the source for the script:

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcode_mp4_files_x265.py

A script to batch transcode .mp4 files using FFmpeg with configurable CRF values.
source: https://gist.github.com/jfrobbins/0f8ef94b1a7ff780f74a320a2fd9530c

############################################################################

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


###############
# example:
#   python transcode_mp4_files_x265.py ./your_directory 28
###############


import os
import sys
import subprocess

# Default CRF value
default_crf_value = 30

# Parse command-line arguments
if len(sys.argv) < 2:
    print("Usage: python transcode_files.py <input_directory> [crf_value]")
    sys.exit(1)

input_dir = sys.argv[1]
crf_value = int(sys.argv[2]) if len(sys.argv) > 2 else default_crf_value

# Resolve the absolute path of the input directory
input_dir = os.path.abspath(input_dir)

# Output directory
output_dir = os.path.join(input_dir, f"crf_{crf_value}")
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# Loop through all files in the input directory
for file in os.listdir(input_dir):
    if file.endswith(".mp4"):  # Only process .mp4 files
        input_file = os.path.join(input_dir, file)

        # Generate the output filename
        file_name, file_ext = os.path.splitext(file)
        output_file = f"{file_name}_crf-{crf_value}{file_ext}"
        output_path = os.path.join(output_dir, output_file)

        # Construct and run the ffmpeg command
        command = [
            "ffmpeg",
            "-i", input_file,
            "-vcodec", "libx265",
            "-crf", str(crf_value),
            output_path
        ]
        print(f"Processing: {input_file} -> {output_path}")
        subprocess.run(command)

```


