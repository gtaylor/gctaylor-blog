---
author: Greg Taylor
pubDatetime: 2011-10-15T03:31:00+00:00
modDatetime:
title: An embarrassing S3 saga
slug: embarrassing-s3-saga
featured: false
draft: false
tags: ["Cloud"]
description: ""
---

Around July of 2009, a post was made to the AWS Developer Forums for S3(which the S3 team reads and responds to) [asking for the
Access-Control-Allow-Origin header](https://forums.aws.amazon.com/thread.jspa?threadID=34281&tstart=0) to be allowed on keys. The primary
motivator for this is that sites would be able to store things like
webfonts in S3.

The S3 team replied shortly after the initial post stating that this
wasn’t in their immediate roadmap, but they’d watch the thread to help
set priorities in the future. Fast-forward over two years, 101 replies,
and 24,000 thread views later and we find ourselves still lacking this
capability. If you look at the [S3 AWS forum](https://forums.aws.amazon.com/forum.jspa?forumID=24&start=0), you’re likely to see
‘[Access-Control-Allow-Origin header](https://forums.aws.amazon.com/thread.jspa?threadID=34281&tstart=0)‘ still near the top.

It’s a shame that a reasonably simple request, which would greatly
improve S3’s utility for webfont-bearing sites, has failed to even get a
“We’re working on this” from the S3 team. We can’t expect them to drop
what they’re doing and get on this, but they’ve remained completely
non-committal on this.

The workarounds
---------------

The way we get around this issue is that we either:

* Serve webfonts from an nginx instance (not ideal, we’re using S3 so
  we don’t have to host media)
* Use a competitor’s service ([Rackspace CloudFiles](http://www.rackspace.com/cloud/cloud_hosting_products/files/)) just for fonts.
  Other CDNs and object stores support this header.
