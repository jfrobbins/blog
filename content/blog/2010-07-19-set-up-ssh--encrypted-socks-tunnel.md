---
authors: Jon Robbins
category: archive
date: '2010-07-19T00:00:00'
draft: false
modified: '2010-07-19T00:00:00'
slug: set-up-ssh--encrypted-socks-tunnel
tags:
- jbs
- encryption
title: set up ssh  encrypted socks tunnel
---

So I had started this a long time ago, and forgotten all about it as I really didn't have a use for it.  Now that I have the ability to [tether](http://factorq.net/2010/07/14/tethering-on-the-moto-droid-with-easytether/" target="_blank), and I have my eeePC working again, combined with attending LUGs--now I have the use for a secure tunnel.

 In case you aren't aware (I wasn't), passwords and logins are sent in PLAIN TEXT--yes, I said plain text.  Nuts, huh?  Anyway, so when you are not on a known or somewhat secure network, this could be dangerous.

 Setting up SSH is very easy to do, and it comes in very handy.  ArchLinux has a [terrific wiki entry](http://wiki.archlinux.org/index.php/SSH" target="_blank), as usual, which speedifies things quite a bit.  It is very straightforward, and I can certainly not do better here.

 There is also a section for [creating an encrypted SOCKS tunnel](http://wiki.archlinux.org/index.php/SSH#Encrypted_Socks_Tunnel" target="_blank).  Once the SSH on the client and SSHd on the host have been configured, creating the tunnel is a breeze.  You just run a command:

 <pre>$ ssh -ND 4711 user@host

 and then configure your web browser:</pre>
<ul>
<li>For Firefox: <em>Edit  Preferences  Advanced  Network  Connection  Setting</em>:</li>
</ul>
<dl><dd>Check the <em>"Manual proxy configuration"</em> radio button, and enter "localhost" in the <em>"SOCKS host"</em> text field, and then enter your port number in the next text field (I used 4711 above).</dd></dl><dl><dd>Make sure you select SOCKS4 as the protocol to use. This procedure will not work for SOCKS5.</dd></dl><dl>
I created a bash alias "sshtunnel" as menoned in the wiki so I have less to type.</dl><dl>Also worth mentioning, is that since my IP is dynamic, and my ssh host computer is behind a router, I have to have some kind of way to broadcast my REAL ip externally.  So, I wen on over to [DynDNS.com](http://DynDNS.com" target="_blank) and set up a free account for a subdmain. Then I just configured my router to forward my ssh port, as well as tell it to update DynDNS with my real IP address when it changes (It has been a built-in feature with my current Netgear as well as my past LinkSys routers).</dl><dl>Very simple, over all.  And it can definitely come in handy.   I have [@NYBill ](http://identi.ca/NYBill" target="_blank)to thank again, he reminded me I needed to finish setting this up.</dl>




tags: #linux 

Tags:  #arch #encrypted #linux #ssh #tether #tunnel 


Published Date: Tue, 20 Jul 2010 02:59:13 +0000 

[Original URL](http://factorq.net/2010/07/19/set-up-ssh-encrypted-socks-tunnel/) | [Original guid](http://factorq.net/?p=365) | PostID= 365

 original filename: 128
