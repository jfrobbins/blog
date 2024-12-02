---
authors: Jon Robbins
category: archive
date: '2011-01-13T00:00:00'
draft: false
modified: '2011-01-13T00:00:00'
slug: got-it-to-work...the-code-display-thing
tags:
- jbs
- site
- blog
- code
- captcha
title: Got it to work...the code display thing
---

So after doing a little work, I got the code tags to work in this blog software. Changes and etc can be found on the site:  [jbs.jrobb.org](http://jbs.jrobb.org).
Now I can post the bulk of the captcha code that I mentioned in my [last post](?article=159).  For the full thing, just download the "jbs" software and check it out. 

Terrible name, by the way: "jbs"--if anyone can think of something better, please let me know!

<b>Captcha stuff</b>

This is PHP, but could probably be used with whatever you want to convert it to:
[code]
function createCaptcha() {
// creates captcha problem and stores along with answer in SESSION vars
//Thanks to @jezra for this:  http://www.jezra.net/blog/creating_a_CAPTCHA

$ip_address = VISITORS_IP; //get the visitors IP address
$appended_ip = $ip_address + date("zB"); //append the numeric day of the year + Swatch Internet time to the ip_address
$salt = "go away spammers"; //add some salt to the appended_ip
$salted_string = $appended_ip+$salt;
$md5_string = md5($salted_string) ; //get the md5sum of the salted string
$first_int = getFirstInt($md5_string); //get the first and last integer of the md5_string
$last_int = getLastInt($md5_string);
//if the first int is greater than the last 
if($first_int>$last_int)
{
//this is a subtraction problem
$problem = $first_int . " minus " . $last_int;
$answer = $first_int-$last_int;
}else{
//this is an addition problem
$problem = $first_int . " plus " . $last_int;
$answer = $first_int+$last_int;
}

//set answer with session var
$_SESSION['canswer'.$problem] = $answer;  
$_SESSION['cproblem'] = $problem;  //set the problem, so can retrieve the answer later
return $problem;
}
[/code]

Looks like this doesn't show up in the rss feed at all...I'll have to fix that in v0.2.1! (edit: fixed now!)

Tags: #site #blog #code #captcha


 original filename: 160