---
author: Greg Taylor
pubDatetime: 2011-10-18T22:22:00+00:00
modDatetime:
title: media-nommer scampers closer to initial release
slug: media-nommer-scampers-closer-initial-release
featured: false
draft: false
tags: ["Python", "Cloud", "Programming"]
description: ""
---

Our Python-based, open source (BSD) distributed encoding system,[media-nommer](http://media-nommer.readthedocs.org/), is inching closer to what we’ll call an initial 1.0
release. We’d love to have other developers take a look, try our
documentation, and help us chase down flaws before we stick a 1.0 on
this thing and put it out there for others to rip to pieces.

Here are the basics:

* An orchestrator/management daemon runs on some arbitrary machine of
  your choice (your own, in EC2, Rackspace, wherever). It provides a
  simple JSON API that your applications can send encoding jobs to. It
  also handles spinning up new instances and communicating job state to
  your applications.
* Encoding nodes are spawned on [Amazon EC2](http://aws.amazon.com/ec2/), with lots of
  configurable options to determine resource usage. The system can
  scale as far as EC2 will let you keep spinning up instances.
* Encoding is handled through “[Nommers](http://media-nommer.readthedocs.org/en/latest/ec2nommerd.html#nommers)“. Each Nommer wraps a
  different kind of encoding software. The only Nommer currently is
  [FFmpegNommer](http://media-nommer.readthedocs.org/en/latest/apiref/ec2nommerd.html#id1), which wraps ffmpeg. We’d love to see some other
  audio and video-related Nommers added (mencoder, anyone?).
* The EC2 encoder nodes are never in direct contact with the master
  management daemon. The management daemon can be stopped and restarted
  at a later date (or on another machine) without any interruptions or
  data loss. No firewall holes needed.

We are dogfooding [media-nommer](http://media-nommer.readthedocs.org/) like crazy on two very large projects
at [DUO](http://duointeractive.com/), and it’s working really well for us. However, we’d love to
have some other eyes and hands on the project, so please do consider
checking it out. If you find yourself using Zencoder or Encoding.com
with any kind of regularity, media-nommer just may save you a lot of money.

* media-nommer ([GitHub Repo](https://github.com/duointeractive/media-nommer), [Documentation](http://media-nommer.readthedocs.org/), [Mailing list](https://groups.google.com/forum/?hl=en#!forum/media-nommer))
* media-nommer-api-python ([GitHub
  Repo](https://github.com/duointeractive/media-nommer-api-python),
  [Documentation](http://media-nommer-api-python.readthedocs.org/))
* IRC Room: #medianommer on FreeNode. I’m gtaylor there.
