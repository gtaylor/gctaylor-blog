---
author: Greg Taylor
pubDatetime: 2011-04-29T03:39:00+00:00
modDatetime:
title: S3 access log parsing/storage with Tamarin
slug: s3-access-log-parsingstorage-tamarin
featured: false
draft: false
tags: ["Python", "Cloud", "Django"]
description: ""
---

We have been helping one of our clients moves their massive collectionof audio and video media to S3 over the last few weeks. After most of
the files were in place, we saw that our usage reports on for one of the
buckets was reporting much higher usage than expected. We ran some CSV
usage report dumps to try to get a better idea of what was going on, but
found ourselves wanting more details. For example:

* Who are the biggest consumers of our media? (IP Addresses)
* What are the most frequently downloaded files?
* Are there any patterns suggesting that we are having our content
  scraped by bots or malicious users?
* How do the top N users compare to the average user in resource consumption.

Enter: Bucket Logging
---------------------

One of S3’s many useful features includes [Server Access Logging](http://docs.amazonwebservices.com/AmazonS3/latest/dev/ServerLogs.html). The
basic idea is that you go to the bucket you’d like to log, enable bucket
logging, and tell S3 where to dump the logs. You then end up with a
bunch of log keys that are in a format that resembles something you’d
get from Apache or Nginx. We ran some quick and dirty scripts against a
few day’s worth of data, but quickly found ourselves wanting to be able
to form more specific queries on the fly without having to maintain a
bunch of utility scripts. We also needed to prepare for the scenario
where we need to automatically block users that were consuming
disproportionately large amounts of bandwidth.

Tamarin screeches its way into existence
----------------------------------------

The answer for us ended up being to write an S3 access log parser with
[pyparsing](http://pyparsing.wikispaces.com/), dumping the results into a Django model. We did the
necessary leg work to get the parser working, and tossed this up on
GitHub as [Tamarin](https://github.com/duointeractive/tamarin). Complete documentation may be found [here](http://duointeractive.github.com/tamarin/).

Tamarin contains no real analytical tools itself, it is just a parser,
two Django models, and a log puller (retrieves S3 log keys and tosses
them at the parser). Our analytical needs are going to be different than
the next person’s, and we like to keep apps like this as focused as
possible. We very well may release apps in the future that leverage
Tamarin for things like the automated blocking of bandwidth hogs we
mentioned, or apps that plot out pretty graphs. However, these are best
left up to other apps so Tamarin can be light, simple, and easy to tweak
as needed.

Going back to our customer with higher-than-expected bandwidth usage, we
ended up finding that aside from a few bots from Nigeria and Canada,
usage patterns were pretty normal. The media that was uploaded into that
bucket was never tracked for bandwidth usage on the old setup, so the
high numbers were actually legitimate. With this in mind, we were able
to go back to our client and present concrete evidence that they simply
had a lot more traffic than previously imagined.

Where to go from here
---------------------

If anyone ends up using Tamarin, please do leave a comment for me with
any interesting queries you’ve built. We can toss some of them up on the
documentation site for other people to draw inspiration from.

**Source:** <https://github.com/duointeractive/tamarin>

**Documentation:** <http://duointeractive.github.com/tamarin/>

**GitHub Project:** <https://github.com/duointeractive/tamarin>
