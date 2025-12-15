---
author: Greg Taylor
pubDatetime: 2016-04-20T00:21:07+00:00
modDatetime:
title: Simple outbound request rate limiting with App Engine
slug: simple-outbound-request-rate-limiting-with-app-engine
featured: false
draft: false
tags: ["Python", "Programming", "Cloud"]
description: ""
---

I've been doing a lot of playing with [Google App Engine](https://cloud.google.com/appengine/) (GAE) of late, since it is a cheap/free way for me to quickly toss ideas against the wall and see what sticks. One of the tinker projects I've been working on is a [sub-Reddit stat tracker](https://github.com/gtaylor/techsubreddits) (warning: hastily put together and un-finished) that records and ranks technical sub-Reddit activity over time.

Retrieving the data I needed required polling the [Reddit API](https://www.reddit.com/dev/api). There is an existing high-quality Python API client ([PRAW](https://praw.readthedocs.org/en/stable/)), but I ran into a [GAE + requests + HTTPS issue](https://github.com/kennethreitz/requests/issues/3018) that prevented me from using it (PRAW uses requests). Said issue will be fixed in requests 2.10.0, but there's been no indication that requests 2.10.0 is arriving anytime soon. This was significant in that PRAW handles rate limiting and oauth authentication for you. Rather than wait for requests 2.10.0 or forking PRAW to use GAE's [urlfetch](https://cloud.google.com/appengine/docs/python/urlfetch/) service (which supports HTTPS), I decided to hit Reddit's public API directly without authenticating.

*Warning: The days of unauthenticated Reddit API access may be [coming to an end](https://www.reddit.com/r/redditdev/comments/3xdf11/introducing_new_api_terms/). I don't recommend unauthenticated API access for anyone doing anything more simple than a tinker project like mine.*

Early goings
------------

My initial draft used App Engine [cron](https://cloud.google.com/appengine/docs/python/config/cron) and [task queues](https://cloud.google.com/appengine/docs/python/taskqueue/) to schedule and parallelize the work. Once an hour, cron triggered a background task that would create sub-tasks for each sub-Reddit I'm tracking. These sub-tasks would hit the Reddit API once or twice, muddle through the return value, and toss some values into a [Custom Metric](https://cloud.google.com/monitoring/custom-metrics/) on Google Stackdriver.

Since the first proof-of-concept wasn't rate limited, I ran into HTTP 429 (Too Many Requests) as I tracked increasingly more sub-Reddits.

![](https://images.squarespace-cdn.com/content/v1/561aafd6e4b02c7f0270ba4f/1461111292671-2KYT4WAUCY5XICKBYJ48/image-asset.png?format=original)

App Engine Queue definitions to the rescue
------------------------------------------

I only needed to do a full scan of all of my tracked sub-Reddits once per hour. I had to make sure that I'm not doing more than 30 API calls per minute. I wanted to try to spread the requests out evenly, rather than exhaust my quota at the beginning of each minute. I also wanted to do this with minimal complexity.

Fortunately, App Engine [task queues](https://cloud.google.com/appengine/docs/python/taskqueue/) can be configured with a [queue.yaml](https://cloud.google.com/appengine/docs/python/config/queue) file in your project root. There are two [directives](https://cloud.google.com/appengine/docs/python/config/queue#Python_Queue_definitions) in here that are particularly interesting:

* **rate** - How often jobs are popped from the queue and distributed to your workers. The number of jobs that are popped at a time is determined by *max\_concurrent\_requests*. For example, a value of 30/m will mean the queue is popped at *most* 30 times per minute.
* **max\_concurrent\_requests** - The max number of concurrently executing jobs.

Since the unauthenticated Reddit API rate limit is 30 requests per minute, I was able to enforce this at the queue level by using a *rate* of 30/m and a *max\_concurrent\_requests* of 1. [Here](https://github.com/gtaylor/techsubreddits/blob/master/queue.yaml) is my full queue.yaml file. The end result:

* Tasks are popped from the queue up to 30 times a minute (*rate = 30/m*).
* We only pop one task at a time (*max\_concurrent\_requests* = 1).
* We won't pop a new task until the currently running one is ACK'd.
* As long as everything works as described in the docs, we stay under the rate limit at all times.

As a result, we went from rate limiting errors all over the place to:

![](https://images.squarespace-cdn.com/content/v1/561aafd6e4b02c7f0270ba4f/1461111168922-Y13UKEVDSNIWBBNKHH98/image-asset.png?format=original)

So you can rate limit. What's the big deal?
-------------------------------------------

Rate limiting is not an especially difficult thing to implement, but I thought it was interesting to see how easy App Engine made this. My code doesn't know or care that it's being rate limited, which is nice. The most beautiful lines of code are the ones you don't have to write at all!

In the future, I'll want to either move over to PRAW when requests 2.10.0 lands or implement the bare minimum for oauth authentication with App Engine's urlfetch service. At that point, I'll be able to twiddle my *rate* and *concurrency* values to get some more throughput.

Nothing earth-shattering here, but I thought I'd share!
