---
authors: Jon Robbins
category: projects
date: '2014-08-28T00:00:00'
draft: false
modified: '2014-08-28T00:00:00'
slug: shortenizer-(link-shortener)
tags:
- projects
title: shortenizer (link shortener)
---
After recently beginning to use [navierstokes](http://polari.us/dokuwiki/doku.php?id=navierstokes) to broadcast my 
social media message across networks (usually originating from my [pump.io](https://io.jrobb.org) ), it became very
apparent to me that the 140 character limit on networks such as twitter and [GNU Social](https://www.gnu.org/software/social/) 
is just archaic and very inconvenient.

I helped out and made some simple test code to post to [ur1.ca](http://ur1.ca) and scrape the html to get the shortened link, 
but I thought I could do something else for myself as a fun project.

So why not write a link shortener?

I've got some particular tastes, though:

* I like [python](https://python.org)
* I *dis*like php
* I also dislike MySQL (& [MariaDB](https://mariadb.org/) )
* I like [SQLite](https://sqlite.org/)
* I wanted some kind of [API](https://en.wikipedia.org/wiki/Application_programming_interface) that would be efficient for automation
* I wanted to be able to (easily) self-host

Those are my feelings for most stuff I run on my own servers, but give and take.

Anyway, I pretty much just used the built-in python http server and set it up behind an [nginx](https://en.wikipedia.org/wiki/Nginx) and 
create simple short links which increment as links are added (each digit allows for 62^(nDigits), 0-9,'A'-'Z', and 'a'-'z' ).
I also added in the code the ability to call from a command line and enter vanity short urls, which I then later implemented in the simple
 web interface and in the api.
 
It is currently in a state that I think is fine to use, however I would like to implement https as a next step.
I'll probably work on getting it integrated into navierstokes first, so that I can have my links automatically shortened using my own service.

Also, it would be cool if some links could be optionally shortened to some vanity term automatically from some content in the target.  
That can be phase 2 (or 3).

If you are interested in checking it out, shortenizer is [on my gitorious](https://gitorious.org/shortenizer).
