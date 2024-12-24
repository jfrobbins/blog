+++
title = 'Making a Favicon'
date = 2024-12-22T10:50:56-05:00
draft = false
tags = ["www","guides"]
+++

# Creating a Multi-Resolution Favicon for Your Website

In today's web environment, having a favicon that looks good across various devices and screen resolutions is crucial. 
Here's a simple guide on how to create a multi-size `favicon.ico` file from a single 128x128 pixel image, using GIMP for resizing and `icoutils` on Ubuntu Linux for the final ICO creation.

## Step 0: Creating an Image
You have to have a starting point, something to actually make an icon from.

I didn't really have anything to use, so I [asked Grok](https://x.com/i/grok/share/5nlRPlZUikzFBIrvZWnMwmC8o) to create some images for me.
As usual, this doesn't go perfectly, but I ended up with one I chose to use after I sized it down to `128x128`:

- ![favicon 128x128](/images/favicon/favicon_128.png)

In the steps below, we'll resize the image several times into the optimal sizes, and then combine them all into one `favicon.ico` file.

## Step 1: Preparing Your Image

### Using GIMP to Resize Your Image

1. **Open Your Image:**
   - Open GIMP and load your 128x128 pixel image by going to `File > Open`.

2. **Resize for Different Resolutions:**
   - For each size you need (16x16, 32x32, 48x48, 64x64), perform these steps:
     - Go to `Image > Scale Image`.
     - Change the `Width` to the desired size (e.g., 16 pixels). The `Height` will adjust automatically if the chain link icon is intact to maintain the aspect ratio.
     - Click `Scale`.
     - Save each resized version:
       - Use `File > Export As...` to save as PNG. Name them accordingly like `favicon_16.png`, `favicon_32.png`, etc.
       
The various size icons:
- ![favicon 64x64](/images/favicon/favicon_64.png)
- ![favicon 48x48](/images/favicon/favicon_48.png)
- ![favicon 32x32](/images/favicon/favicon_32.png)
- ![favicon 16x16](/images/favicon/favicon_16.png)

## Step 2: Creating the ICO File with icoutils

### Install icoutils on Ubuntu

Before proceeding, make sure you have `icoutils` installed:
```bash
sudo apt-get update
sudo apt-get install icoutils
```


### Combine PNGs into One ICO File
With your PNG files ready, use icotool from icoutils to create the .ico file:

```
bash

icotool -c -o favicon.ico favicon_16.png favicon_32.png favicon_48.png favicon_64.png favicon_128.png
```

- `-c` creates a new ICO file.
- `-o` specifies the output file name.


### Verify Your ICO File
You can check the contents of your .ico file to ensure all sizes are included:

```
bash

icotool -l favicon.ico
```

Here is my output:

```
$ icotool -l favicon.ico 
--icon --index=1 --width=16 --height=16 --bit-depth=8 --palette-size=256
--icon --index=2 --width=32 --height=32 --bit-depth=24 --palette-size=0
--icon --index=3 --width=48 --height=48 --bit-depth=24 --palette-size=0
--icon --index=4 --width=64 --height=64 --bit-depth=24 --palette-size=0
--icon --index=5 --width=128 --height=128 --bit-depth=24 --palette-size=0
```

## Step 3: Implementing the Favicon on Your Site

- Place the File: Move your `favicon.ico` to the root directory of your website.
- Reference in Your Site:
  - For Jekyll, add to `_includes/head.html`:
```  
        html

        <link rel="icon" type="image/x-icon" href="/favicon.ico">
```

  - For Hugo, you might adjust your theme's `head.html` or set in `config.toml`:
```  
        toml

        [params]
          favicon = "/favicon.ico"
```

## Conclusion
Creating a multi-resolution favicon ensures your site looks professional on various platforms and devices. 
By using GIMP for resizing and icoutils for combining, you achieve this with free, open-source tools on Linux. 

Remember, simplicity in your original design can help maintain clarity when scaling down to smaller sizes.

## a little help
[grok helped me](https://x.com/i/grok/share/4e7Yz0PUK7vmvsbguVnas6lhA) with the details a bit, and I'm documenting this how-to here.

I also made a [github gist](https://gist.github.com/jfrobbins/7a579fe888b08612f892db759db2ed13)
