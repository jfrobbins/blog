---
authors: Jon Robbins
category: archive
date: '2011-02-13T00:00:00'
draft: false
modified: '2011-02-13T00:00:00'
slug: version-control-synopsis-git-vs-fossil
tags:
- jbs
- git
- work
title: Version Control synopsis git vs fossil
---

I've mentioned recently that I [started using Git](?article=161) for my version control needs.  
This has worked out well for me, both on my personal projects at home (mostly this blog stuff), and at work.

Now at work in my department we only have two software guys: another guy and myself.  
We both have a few independent projects, and then we have one main one where we overlap on bug fixes and things.
On this project, the other guy is the lead. Anyway, we had talked about version control for a while because of the sheer amount of bug fixes and additions that have been going on.  If I make changes for a fix, or implement a new test procedure or anything, what I currently have to do is send the changes in some kind of text format to him and then he manually implements the changes.  Hardly efficient, but it has worked okay up until this point.  Now this whole project is so big and complex it has become very tedious and time consuming to do it this way.

I have been using [git](http://git-scm.com/), and love it.  Steve (the other guy) has heard of [fossil](http://www.fossil-scm.org/index.html/doc/trunk/www/index.wiki), and wanted me to evaluate these two main contenders.  While I did this testing, I took LOTS of notes, and this post will basically show what I came up with.

Go ahead and skip it if you aren't already interested :-)

<!--more-->

First, I am going to go ahead and say that these two version control systems are very similar but also very different. They handle things slightly differently, but ultimately accomplish the same goal.

Fossil aims to be simple to install and use, while being compact and efficient. It has a built-in web server as a UI, and is contained in a single binary executable.  Revisioning info stuff is stored in a SQLite database.

Git is much bigger and complex, requires an actual install and uses many more commands. The windows version comes with a GUI (not too impressive to me since I like the console, but Steve likes the idea of a GUI).  Revisioning info stuff is stored in what can be referred to as a "pile of files."

Many of the commands between the two are the same, although some of them have different characteristics.  I will mostly cover the glaring differences here, and my final conclusions.  Maybe I will upload my mass amounts of notes later on as well. 

<i>edit:</i> I have uploaded my notes, in their respective repo formats. They contain only text files of my notes as I went along using the two systems and comparing them, as well as simple merge tests and such: [fossil_test.tar.gz](/xfer/code/test/fossil_test.tar.gz) and [git_test.tar.gz](/xfer/code/test/git_test.tar.gz)

<i>git</i> 

<ul>
<li>commit is local only</li>
<li>only pushes the current (or specified branch</li>
<li>on push, if remote version is newer it notifies and lets you know to do a pull (fetch+merge)</li>
<li>branches are easy to create, AND easy to delete</li>
</ul>

<i>fossil</i>
 
<ul>
<li>operates more like SVN or CVS with autosync on</li>
<li>commit ALSO pushes to remote (autosync ON)</li>
<li>update (branch) also pulls from remote repo (autosync ON)</li>
<li>pushes ALL branches, unless they are private</li>
<li>pushing when repo is newer does NOT notify, and just replaces the head (autosync OFF)</li>
<li>I could not ever figure out how to DELETE a branch</li>
<li>IMO the UI is useless if not used on a remote http web server/repo (not the way we use it, on a remote windows drive)</li>
</ul>

<b>In conclusion</b>, they are both fine programs that works as they are supposed to, however I still prefer git. It operates in an expected manner and "just makes sense" to me.  Fossil, I think is okay as long as autosync is ON--when it is off, I think it would be difficult to keep track of revision changes since it does not notify if trunk/HEAD is actually newer than what you are pushing.  Also it is incredibly irritating that it is so difficult (if possible at all) to delete unwanted branches.  This is discouraging for those who like to make new branches rather than working in trunk, or just a number of specified branches ( like to create branches and then just delete them after I merge them in or if they don't work out).

I have given my synopsis to him, however I'm not sure yet which steve will choose. Either way will be better than manually entering all of these changes!


taggage: #git #fossil #scm #version-control #work #code

Also, I'll add that in Windows (our work environment), I have found it much easier to use [Console2](http://sourceforge.net/projects/console/) instead of the default windows shell. I also point it either to a [Cygwin](http://www.cygwin.com/) or [mingw](http://www.mingw.org/) bash.  Git comes with a mingw shell.  This makes it much more "at home," and enables the use of standard linux bash shell commands.  And Console2 is resizeable, unlike the standard windows prompt window!

 original filename: 164
