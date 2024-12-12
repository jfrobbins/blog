---
authors: Jon Robbins
category: server
date: '2014-09-01T00:00:00'
draft: false
modified: '2014-09-01T00:00:00'
slug: moving-my-pump-home
tags:
- server
- pumpio
title: moving my pump home
---
I was suspended from my vps again sometime yesterday due to going over my 3TB monthly bandwidth limit 
-- I was seeding many linux distributions, and with the fat pipes on the vps it just happened. 
I'll have to be more careful in the future.

Anyway, this was a good opportunity for me to stop depending on the vps for my social networking at least, 
and I decided to go ahead and move my [pump](http://pump.io) from the vps onto one of my home servers.

Since pump.io is intended to be run in a standalone type fashion bound directly to port 80/443 and I have other services running
 (web, etc), I had to setup my pump server behind a proxy.
 
I'm using [nginx](http://nginx.com/), which is awesome.  
And luckily [sazius](http://www.sjoberg.fi/blog/pumpio.html) and [jpope](http://whird.jpope.org/pump/) have done the whole proxy setup thing before so this is old hat.

I wanted to document what I did so that I remember if I have to do this again. Plus this is an easy way to view my configs.
Here's a [link](http://nginx.com/blog/websocket-nginx/) or [two](http://nginx.org/en/docs/http/websocket.html) about websocket proxying.

## setup

Here are the versions of things that I'm currently using:

* [nodejs](http://www.nodejs.org/) v0.10.25 (from the ubuntu LTS repos)
* npm v1.3.10
* mongod v2.4.9
* nginx 1.4.6
* pump.io something around v0.3.0 and like jpope, I'm using a free ssl cert from [startSSL](https://www.startssl.com/)

## db

jpope uses redis db and seems ok with it, however I've used it before and [ran into some 
problems]({filename}/blog/2013-12-07-raspi-pump-the-end.markdown) as redis keeps the entire db in memory.
  Not that mongodb is flawless, there's also a [problem with 32-bit]({filename}/blog/2014-03-13-mongodb-problem-with-x86.markdown), but that is 
easily 
solved.
  So, I installed mongodb from the repos and left it at its defaults.
  
## pumpio

bunyan and forever are some node tools that are *very* useful with keeping things running and debugging.

    # npm install -g bunyan
    # npm install -g forever

forever restarts and keeps a process running if it crashes.
bunyan makes the log files look pretty.

	{
		"driver":  "mongodb",
		"params":  {"dbpath": "/srv/pump.io/db/"},
		"secret":  "erhmagerditsasercrert",
		"noweb":  false,
		"site":  "io.jrobb.org",
		"owner":  "Jon Robbins",
		"ownerURL":  "http://jrobb.org/",
		"port":  4443,
		"urlPort":443,
		"bounce": false,
		"hostname":  "io.jrobb.org",
		"address":  "127.0.0.1",
		"nologger":  false,
		"serverUser":  "pumpio",
		"key":  "/path/to/ssl.key",
		"cert":  "/path/to/ssl.crt",
		"uploaddir": "/srv/pump.io/uploads",
		"debugClient": false,
		"compress": true,
		"firehose": "ofirehose.com",
		"noCDN":false,
		"requireEmail": false,
		"disableRegistration": true,
		"canUpload": true,
		"sockjs": true
	}

looks like jpope added his user like this:

    # useradd -s /bin/bash -d /srv/http/pump.jpope.org
    
whereas I did this:

    # useradd -M pumpio
    
then chowned my /srv/pump.io dir to that 'pump.io user.

his way might be better.

I start my pump by running this simple bash script so I don't have to remember the syntax:
    
     #!/bin/bash
	 #/srv/pump.io/startpump.sh
	 sudo forever start -al /srv/pump.io/logs/pump.log /srv/pump.io/bin/pump
	
To stop the pump, simply:

	sudo forever stopall

or you could `forever list` and `forever stop 0` (or whatever index it is).
	
## nginx

As I mentioned, I'm using nginx which seems to be the way to go.

	##########################################################
	# /etc/nginx/conf.d/io.jrobb.org.conf

	upstream pumpbackend {
	  server 127.0.0.1:4443 max_fails=3 fail_timeout=30s;
	  server 127.0.0.1:4443 max_fails=3 fail_timeout=60s;
	  server 127.0.0.1:4443 max_fails=3 fail_timeout=90s;
	}
	server {
	  listen 80;
	  server_name io.jrobb.org;
	  rewrite ^ https://io.jrobb.org$request_uri?;
	}

	map $http_upgrade $connection_upgrade {
		default upgrade;
		''      close;
		}

	server {
	  listen 443 ssl;
	  server_name io.jrobb.org;

	  access_log  /var/log/nginx/pump.access.log;
	  error_log  /var/log/nginx/pump.error.log debug;

	#  # this is the important chunked encoding stuff
	#  #only for nginx <= 1.3.9 http://wiki.nginx.org/HttpChunkinModule
	#  chunkin on;
	#  error_page 411 = @my_411_error;
	#  location @my_411_error {
	#    chunkin_resume;
	#  }

	  ssl_stapling on;
	  ssl_trusted_certificate /etc/nginx/ssl/sub.class1.server.ca.pem;
	  ssl_certificate      /srv/pump.io/ssl/ssl.io.jrobb.org.unified.crt;
	  ssl_certificate_key  /srv/pump.io/ssl/ssl.io.jrobb.org.key;

	  include shared/global.conf;
	  client_max_body_size 6m;

	  keepalive_timeout 75 75;
	  gzip_vary off;

	  location / {
		proxy_pass https://pumpbackend;
		proxy_http_version 1.1;
		proxy_redirect off;
		proxy_set_header Upgrade $http_upgrade;
		proxy_set_header Connection $connection_upgrade;
		proxy_set_header Host $http_host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_buffers 16 32k;
	  }
	}

in sazius' post, he mentions the chunkin settings, but that doesn't appear to be necessary in nginx versions > 1.3.9

	##########################################################
	# /etc/nginx/shared/global.conf

	location = /favicon.ico {
		try_files $uri = 204;
		log_not_found off;
		access_log off;
		expires max;
	  }

	  location = /robots.txt {
		allow all;
		log_not_found off;
		access_log off;
	  }

	  location ~ /\.ht {
		deny all;
		access_log off;
		log_not_found off;
	  }

	  location ~* ^.+\.(bzr|git|log)$ {
		access_log off;
		log_not_found off;
		return 444;
	  }

	  location ~* ~$ {
		access_log off;
		log_not_found off;
		return 444;
	  }

	  error_page 500 502 503 504 /50x.html;
	  location = /50x.html {
		root /usr/share/nginx/html;
		internal;
	  }
	  error_page 404 /404.html;
	  location = /404.html {
		root /usr/share/nginx/html;
		internal;
	  }
	  error_page 403 /403.html;
	  location = /403.html {
		root /usr/share/nginx/html;
		internal;
	  }

## running

That gets everything up and running (or should).  Check the nginx access and error logs for the pump entries.
Also, to check the pump log using bunyan I just run this file (and edit the level to detect errors vs info):

	#!/bin/bash
	#/srv/pump.io/viewlog.sh
	#tail -f logs/pump.log | bunyan -l 30
	tail -f logs/pump.log | bunyan -l 40
	
Level 30 is info, and level 40 are errors only.  20 is probably debug. No flag is everything, I believe.

I'm seeing a few "proxy failed" errors in my logs, but that seems to be normal.
Everything is still working as it was before (on the vps!).

A note about the transfer, I had backups of my db, config files and everything.
It would not be possible to transfer a host without the same secret key and db (or at least the information that was in the db).


## backups

For those interested, here's the script I run in a cronjob once or twice a week:

	#!/bin/bash
	#~/scripts/vpsbackup-daily-root.sh
	
	DATE=$(date +"%Y%m%d")
	BAKDIR='/my/backups/dir'
	TMPDIR=$BAKDIR/DAILY
	TARFLAGS='czvf'
	EXT='tgz'
	#TARFLAGS='cJvf'
	#EXT='tar.xz'

	BIGEXT='tgz' #total wrapper
	FNAME='daily'
	PREVIOUS='previous'

	#if ! (($(date +"%d") % 2)); then
	#	FNAME="daily"
	#else
	#	FNAME="daily"
	#fi


	#stop the pump to not interfere with backups
	cd /srv/pump.io
	forever stopall &
	wait

	mkdir $TMPDIR
	cd $TMPDIR

	touch $DATE.date

	#copy come config file backups:
	cp /etc/nginx/sites-available/default ./etc-nginx-sites-available-default
	cp -r /etc/nginx/conf.d ./
	cp /etc/pump.io.json ./etc-pump.io.json
	cp /home/jon/scripts ./

	#targzip whole dirs:
	tar -$TARFLAGS $DATE-srv.$EXT /srv/* --exclude=/srv/minecraft/map/*
	tar -$TARFLAGS $DATE-varlib-mongo.$EXT /var/lib/mongodb/*
	tar -$TARFLAGS $DATE-home-scripts.$EXT /home/jon/scripts

	#tarball it all up:
	cd ..

	#save the previous file (keep 2 backups)
	mv $FNAME.$BIGEXT $PREVIOUS.$BIGEXT

	tar -czvf $FNAME.$BIGEXT $TMPDIR
	rm -rf $TMPDIR

	chown jon:jon $FNAME.tgz

	#start the pump back up
	cd /srv/pump.io
	echo '' > /srv/pump.io/logs/pump.log   #clear the log


	forever start -al /srv/pump.io/logs/pump.log /srv/pump.io/bin/pump



![PiPump](/images/rasPiPump.jpg)


# HPR podcast - hacker public radio

NYBill and I recorded this episode:
- [nybill_jrobb-pipump.ogg](/audio/nybill_jrobb-pipump.ogg)
