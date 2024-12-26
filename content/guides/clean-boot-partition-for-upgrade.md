+++
title = 'Clean Boot Partition for Upgrade'
date = 2024-12-25T22:35:59-05:00
draft = false
tags = ["guides"]
+++

Every time my laptop upgrades, I need to clear /boot so the kernels can update.
I put this into a [gist](https://gist.github.com/jfrobbins/100324115ca38a89c07185213a77b634) so I can easily find it and do it again since I can never remember what to do (lol).

# Clean up /boot
- Source link: https://askubuntu.com/questions/345588/what-is-the-safest-way-to-clean-up-boot-partition

First check your kernel version, so you won't delete the in-use kernel image, running:

`uname -r`

Now run this command for a list of installed kernels:

`dpkg --list 'linux-image*' | grep ^ii`

and delete the kernels you don't want/need anymore by running this:

`sudo apt-get remove linux-image-VERSION`

Replace VERSION with the version of the kernel you want to remove.

When you're done removing the older kernels, you can run this to remove ever packages you won't need anymore:

`sudo apt-get autoremove`

And finally you can run this to update grub kernel list:

`sudo update-grub`
