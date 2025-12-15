---
author: Greg Taylor
pubDatetime: 2009-09-04T13:47:00+00:00
modDatetime:
title: Fun with MDSChannelPeerCreate errors on Mac OS X Server
slug: fun-with-mdschannelpeercreate-errors-on-mac-os-x-server
featured: false
draft: false
tags: ["Mac"]
description: ""
---

We started experiencing AFP problems and general instability on one ofour Mac OS X servers today. AFP locked up and sucked a lot of resources,
caused some bogus error messages in the logs. Kept getting this in particular:

AppleFileServer[4806] MDSChannelPeerCreate: (os/kern) invalid argument

It looks like this may be due to a permissions problem on one of the
root drives our AFP server is making available to clients. Looking at
the files within the .fseventsd directory on the drive’s mount
point, I noticed that everything beneath .fseventsd was owned by
root:unknown. Recursively chown’ing this to root:staff and setting
permissions to 770 seems to have stopped the errors and returned
stability after restarting AFP.

This was one of those problems that Googling didn’t yield a good answer
to initially. I really had to dig and though I’d post this up for others
to see. Make sure you post a comment if this helped you.
