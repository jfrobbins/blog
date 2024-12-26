+++
title = ' Create mp4 from Images'
date = 2024-12-25T22:35:59-05:00
draft = false
tags = ["guides"]
+++


This is mostly sourced from the url here:
- https://stackoverflow.com/questions/24961127/how-to-create-a-video-from-images-with-ffmpeg

Which I then put into [this gist](https://gist.github.com/jfrobbins/49e2b53b155bfb77aa426859134d3ff6).
And now this post.

# Create mp4 from Images


`-pattern_type glob`

This great option makes it easier to select the images in many cases.

Normal speed video with one image per frame at 30 FPS

create mp4 from pictures in a directory:
`ffmpeg -framerate 30 -pattern_type glob -i '*.png' \
  -c:v libx264 -pix_fmt yuv420p out.mp4`
  
  
  same but add audio to it:
  ```
  ffmpeg -framerate 30 -pattern_type glob -i '*.png' \
  -i audio.ogg -c:a copy -shortest -c:v libx264 -pix_fmt yuv420p out.mp4
  ```
  
  
  
Slideshow video with one image per second
```
ffmpeg -framerate 1 -pattern_type glob -i '*.png' \
  -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
```


Be a hippie and use the Theora patent-unencumbered video format in an OGG container:
```
ffmpeg -framerate 1 -pattern_type glob -i '*.png' -i audio.ogg \
  -c:a copy -shortest -c:v libtheora -r 30 -pix_fmt yuv420p out.ogv
```


Your images should of course be sorted alphabetically, typically as:
```
0001-first-thing.jpg
0002-second-thing.jpg
0003-and-third.jpg
```


