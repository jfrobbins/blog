---
authors: Jon Robbins
category: archive
date: '2011-01-14T00:00:00'
draft: false
modified: '2011-01-14T00:00:00'
slug: gitting-started
tags:
- jbs
- git
title: Gitting started
---

It is a bit embarassing for me to admit this, but I having been using Linux for 10ish years now, and I have never used [Git](http://git-scm.com/) until very recently.
Sacrilege, I know!  Other version control systems I have also stayed away from--except for [launchpad](https://launchpad.net/)/[bazaar](https://launchpad.net/bzr), which I used I think 3 commands but never really got into it.

When I started hacking into my [blog software](http://jbs.jrobb.org), I started realizing that some sort of version control would definitely come in handy even though it is just rather simple PHP.  
There are many different version controls in addition to the ones I listed above (like SVN, CVS,...it really does go on and on) but on the [LinuxOutlaws forum](http://forums.linuxoutlaws.com/viewtopic.php?f=10&t=2995&hilit=gitorious), there was a discussion, but everyone seems to have a different opinion but github and gitorious were pretty well liked.
I looked around at a few of them, and decided that git looked like it makes the most sense to me.  And then I decided to go with [gitorious](http://gitorious.org/jbs)--what can I say, it's a pretty cool name. :-)

[Github](https://github.com/) looks good also, but apparently their framework isn't open source or something, which is unfortunate.  Ultimately it just comes down to user preference.

I thought that using git would be hard to get used to, but after a couple of days (and one of those spent perusing through [gitref.org](http://gitref.org)), now git is second nature.  Of course...I still haven't done anything complicated with it--mostly just some branches/merges and lots of commits and pushes.

Today, as I was back at work and merging a bunch of our internal code stuff that I had edited (it is in VB6, currently), I realized that this was really just a ridiculous hassle to do manually.  If I make some improvements, I usually have to either keep track of what I change, or go through after the fact doing file compares and compiling the changes to send to the other guy to include in his code.  Not very efficient you say?  Yeah...I know.

This time I made use of the "diff" program on my cygwin shell, which made file-compare on the entire directory pretty easy.  I would have tried to use patch as well, but my co-worker had some other things that he needed to add in as well.

Anyway...why not use Git?!

I went to the Git website and downloaded a Windows version, which came with some kind of GUI that isn't very productive. Luckily, it installed a git bash shell, so actual use is very similar to using it on my linux machines here at home.
I then set up a remote repository on one of my backup servers, and local repository.  and bam presto! all was gravy.

I even set this up on another one of my computers there, so that I can merge my code no matter where I am editing it.  
Hopefully this will save me from a lot of wasted time. I'm betting so, since I usually go ad try to add features a few different ways and sometimes stuff doesn't work out--with Git I can just delete that branch, and keep the other code intact! 

The "bloated software department" uses perforce, but they haven't quite come to take us over yet with their .NET monstrosity.
hopefully they won't ever...but that's another story.

As long as I am able I will promote free and open software in my workplace (when applicable).

To sum up... I love Git!

Tags: #Git

 original filename: 161
