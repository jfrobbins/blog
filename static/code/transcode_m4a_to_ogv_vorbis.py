#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
transcode_m4a_to_ogv_vorbis.py

A script to batch transcode .m4a files to .ogv with Vorbis audio using FFmpeg, 
allowing for both CBR and VBR settings for file size optimization.

Based on:
- https://gist.github.com/jfrobbins/0f8ef94b1a7ff780f74a320a2fd9530c
- https://jrobb.org/guides/transcode-mp4-videos-to-x265-and-lower-bitrate/

With help from Grok:
- https://x.com/i/grok/share/FfeSNTDr2A8gNRXE0pHEsUD5c

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
#   python transcode_m4a_to_ogv_vorbis.py ./your_directory [bitrate] [mode]
#   python transcode_m4a_to_ogv_vorbis.py ./your_directory 128k cbr
#   python transcode_m4a_to_ogv_vorbis.py ./your_directory 2 vbr
#		(lower numbers are lower file sizes)
#   - Default bitrate is 128k if not specified
#   - Default mode is 'cbr', use 'vbr' for variable bitrate
###############


import os
import sys
import subprocess

# Default settings
default_bitrate = "128k"
default_mode = "cbr"

# Parse command-line arguments
if len(sys.argv) < 2:
    print("Usage: python transcode_m4a_to_ogv_vorbis.py <input_directory> [bitrate] [mode]")
    print("  - bitrate: e.g., 128k (default: 128k)")
    print("  - mode: 'cbr' for constant bitrate or 'vbr' for variable bitrate (default: cbr)")
    sys.exit(1)

input_dir = sys.argv[1]
bitrate = sys.argv[2] if len(sys.argv) > 2 else default_bitrate
mode = sys.argv[3].lower() if len(sys.argv) > 3 else default_mode

# Validate mode
if mode not in ["cbr", "vbr"]:
    print("Invalid mode. Use 'cbr' for constant bitrate or 'vbr' for variable bitrate.")
    sys.exit(1)

# Resolve the absolute path of the input directory
input_dir = os.path.abspath(input_dir)

# Output directory
output_dir = os.path.join(input_dir, "ogv")
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# Loop through all files in the input directory
for file in os.listdir(input_dir):
    if file.endswith(".m4a"):  # Only process .m4a files
        input_file = os.path.join(input_dir, file)

        # Generate the output filename with .ogv extension
        file_name, _ = os.path.splitext(file)  # ignore m4a extension
        output_file = f"{file_name}.ogv"
        output_path = os.path.join(output_dir, output_file)

        # Construct the ffmpeg command based on the mode
        if mode == "cbr":
            command = [
                "ffmpeg",
                "-i", input_file,
                "-c:a", "libvorbis",  # Vorbis audio codec
                "-b:a", bitrate,      # Set the audio bitrate (CBR)
                output_path
            ]
        else:  # VBR mode
            command = [
                "ffmpeg",
                "-i", input_file,
                "-c:a", "libvorbis",  # Vorbis audio codec
                "-q:a", bitrate,      # Use quality setting for VBR (bitrate here acts as quality; lower number means higher quality)
                output_path
            ]

        print(f"Processing: {input_file} -> {output_path} with {mode.upper()} mode and bitrate/quality {bitrate}")
        subprocess.run(command)
