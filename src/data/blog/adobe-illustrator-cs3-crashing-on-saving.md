---
author: Greg Taylor
pubDatetime: 2008-04-30T04:02:00+00:00
modDatetime:
title: Adobe Illustrator CS3 Crashing on Saving
slug: adobe-illustrator-cs3-crashing-on-saving
featured: false
draft: false
tags: []
description: ""
---

After trying to figure out why Illustrator CS3 kept crashing when savingfiles, I finally turned up [this bit of information](http://www.adobeforums.com/webx/.3bc3dfb9) that pointed me in
the right direction. It looks like if you have your Print Spooler
service on Windows XP disabled when attempting to save, Illustrator dies.

One of the posters on the linked thread mentions setting your default
printer to Adobe PDF if you still have problems when your printer is off
(but your Spooler Service is on). I am able to save while my printer is
off without a problem, but disabling the Spooler service and setting my
default printer to Adobe PDF still results in a crash.

Things to glean from this:

* On Windows XP, your Print Spooler service must be active to avoid crashes.
* I don’t think your printer needs to be on (at least this was the case
  with mine).
* If you do have problems with saving while your printer is in an
  abnormal state, set your default printer to Adobe PDF.

Hopefully this is useful to someone out there.
