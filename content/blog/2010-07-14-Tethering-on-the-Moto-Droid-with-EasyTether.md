---
authors: Jon Robbins
category: archive
date: '2010-07-14T00:00:00'
draft: false
modified: '2010-07-14T00:00:00'
slug: tethering-on-the-moto-droid-with-easytether
tags:
- jbs
- linux
- android
- droid
- easytether
- tether <br>
title: Tethering on the Moto Droid with EasyTether
---

This is really great, and extremely easy.  I have [NYBill](http://identi.ca/NYBill" target="_blank) to thank for finding out about this.

 There is a tutorial from [here](http://www.debiantutorials.org/ezsurfer-blog/356-tether-a-droid-alternatives" target="_blank), However, in case that goes away I will list the steps here (in the very likely event I forget how to connect).

 EasyTether is in the Android Market  (as well as an EasyTether Lite, which can't connect to https, among other things).

 Once you install and run the app, it can download the driver file which is a .deb package.  There are also windows drivers, but I don't know anything about those...

 Anyway, connect to usb, and enable the usb so that the phone is mountable. copy or install the .deb from the phone.

 After installation, UnMount the phone (leaving the USB connected) and start EasyTether on the Droid.

 On the PC, open a terminal and type

 <pre>easytether enumerate</pre>
This returns an ID of the device.  Capture this ID and paste it into the ##### in the command below:

 <pre>easytether connect #####

 </pre>
This will connect the droid, as well as give you a command which you need to type into another terminal to configure the connection.  This command needs to be entered into a separate terminal window, which can be closed after this command is executed.  *The first window needs to stay open!

 <pre>sudo dhclient easytether0</pre>
The second terminal window can now be closed.  The first window needs to be left open for the entire session, and when you wish to disconnect, this can be done by pressing CTRL-C in that first terminal window to exit.

 <strong>Update:</strong>
In order to make my life easier, I made a couple of entries into my ~/.bashrc file for these commands:

 <pre>alias tetherinit="easytether enumerate | easytether connect"

 alias tetherstart="sudo dhclient easytether0"

 </pre>
(as of this writing, this method still works with Android 2.2)

 <div id="_mcePaste" style="position:absolute;left:-10000px;top:160px;width:1px;height:1px;overflow:hidden;">
easytether connect ################

 e

 </div>




tags: #linux 

Tags:  #android #droid #easytether #tether 


Published Date: Wed, 14 Jul 2010 15:32:50 +0000 

[Original URL](http://factorq.net/2010/07/14/tethering-on-the-moto-droid-with-easytether/) | [Original guid](http://factorq.net/?p=352) | PostID= 352

 original filename: 125