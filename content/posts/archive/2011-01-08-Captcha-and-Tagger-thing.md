---
authors: Jon Robbins
category: archive
date: '2011-01-08T00:00:00'
draft: false
modified: '2011-01-08T00:00:00'
slug: captcha-and-tagger-thing
tags:
- jbs
- site
title: Captcha and Tagger thing
---

So I wanted to enable the commentation on my blog, but hl-- does not incorporate any spam control by default.  
Luckily, however, [@jezra](http://identi.ca/jezra) has [made a post](http://www.jezra.net/blog/creating_a_CAPTCHA) on this very same subject in the past.

Using his code adapted into my php stuffs, it appears to work perfectly!

I did go back as Jezra suggested and convert it to use a SESSION variable, I also made it change the problem more often.

Then I went back and added an email feature so that if it is enabled, I am sent an email if a comment is posted.

I am now realizing that I need a way to tag quotes and "code" type sections in order to display them properly, otherwise it just looks like crap.
That will definitely be my next project for this thing.

Also, I made a ["tag cloud"](tags.php) page that just displays and links all of the tags. I wanted to this because it's an easy way to categorize all of the posts, since hl-- does not have any categories or even tags by default.
This was pretty easy to do, using the standard tag designation "#" (although I made it so that it could be customized).  This tag generator thing just iterates through all of the posts searching for tags and puts them in an array, then links them--pretty easy stuff.
If I get that code formatty thing working, I'll post up how I did this, although there's nothing amazing to it.  I'm sure somebody could use it though, especially if using a simple blog program like hlscript or [hl--](http://www.cockos.com/hl--/).

Maybe I will even make a git or launchpad for "my" version of this hl-- blog software (which is probably now more like the original hlscript).  hl++?

By the way, as if it isn't obvious, I am decent at programming but terrible at design.  This site looks pretty awful, but I'll call it "spartan and utilitarian" :-)


Tags: #site #tags #captcha #blog


 original filename: 159
