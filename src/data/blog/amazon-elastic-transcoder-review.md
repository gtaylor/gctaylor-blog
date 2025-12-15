---
author: Greg Taylor
pubDatetime: 2013-01-30T20:37:00+00:00
modDatetime:
title: Amazon Elastic Transcoder Review
slug: amazon-elastic-transcoder-review
featured: false
draft: false
tags: ["Python", "AWS", "Reviews", "Pathwright"]
description: ""
---

[Amazon Elastic Transcoder](http://aws.amazon.com/elastictranscoder/) was released just a few short days ago.Given that we do a lot of encoding at [Pathwright](http://www.pathwright.com), this was of high
interest to us. A year or two ago, we wrote [media-nommer](https://media-nommer.readthedocs.org) which is
similar to Amazon’s Transcoder, and it has worked well for us. However,
as a small company with manpower constraints we’ve had issues finding
time to continue maintaining and improving media-nommer.

With the hope that we could simplify and reduce engineering overhead, we
took the new Elastic Transcoder service for a spin at Pathwright.

Web-based management console impressions
----------------------------------------

One of the strongest points of the AWS Elastic Transcoder is its web
management console. It makes it *very* easy for those that don’t have
the time or capability to work with the API to fire off some quick
transcoding jobs. With that said, I will make a few points:

* At the time of this article’s writing (Jan 30, 2013), it is extremely
  tedious to launch multiple encoding jobs. There’s a lot of typing and
  manual labor involved. For one-off encodings, it’s great.
* Transcoding presets are easy to set up. I appreciate that!
* Some of the form validation Javascript is just outright broken. You
  may end up typing a value that isn’t OK, hitting “Submit”, only to
  find nothing happen. The probable intended behavior is to show an
  error message, but they are very inconsistently rendered
  (particularly on the job submission page).
* The job status information could be a lot more detailed. I’d really
  like to see a numerical figure for how many minutes AWS calculates
  the video to be, even if this is only available once a job is
  completed. This lets you know exactly how much you’re being billed
  for on a per-video basis. Currently, you just get a lump sum bill,
  which isn’t helpful. It’d also be nice to see when an encoding job
  was started/finished on the summary (you can do this by listening to
  an SNS topic, but you probably aren’t doing that if you’re using the
  web console).

Web API impressions
-------------------

For the purpose of working Elastic Transcoder into [Pathwright](http://www.pathwright.com), we
turned to the excellent [boto](http://boto.cloudhackers.com/) (which we are regular contributors
to). For the most part, this was a very straightforward process, with
some caveats:

* The transcoding job state SNS notifications contain zero information
  about the encoding minutes you were billed for that particular job.
  In our case, we bill our users for media management in Pathwright, so
  we must know how much each encoding job is costing us, and who it
  belonged to. Each customer gets a bill at the end of the month,
  without needing to hassle with an AWS account (these aren’t technical
  users, for the most part). Similarly, the “get job” API request shows
  no minutes figure, either.
* If you’re writing something that uses external AWS credentials to
  manage media, you’ve got some setup work to do. Before you can submit
  job #1, you’re going to need to create an SNS topic, an IAM role, a
  Transcoder Pipeline, and any presets you need (if the defaults aren’t
  sufficient). If you make changes to any of these pieces, you need to
  sync the changes out to every account that you “manage”. These are
  all currently required to use Transcoder. This is only likely to be a
  stumbling block for services and applications that manage external
  AWS accounts (for example, we encode videos for people, optionally
  using their own AWS account instead of ours).
* At the time of this article’s writing, the documentation for the web
  API is severely limited. There is a lack of example request/response
  cycles with anything but one or two of the most common scenarios. I’d
  like to see some of the more complex request/responses.

Some general struggles/pain points
----------------------------------

While this article has primarily focused on the issues we ran into,
we’ll criticize a little more before offering praise:

* As is the case for anyone not paying money for premium support, **AWS
  has terrible customer support**. If you want help with the
  Transcoding service, the [forums](https://forums.aws.amazon.com/forum.jspa?forumID=147&start=0) are basically your only option.
  The responses seen in there so far haven’t been very good or timely.
  However, it is important to note that this support model is not
  limited to Elastic Transcoder. It is more of an organizational
  problem. I am sure this is on their minds, and if there is a group
  that can figure out how to offer decent support affordably, it’d
  be Amazon. Just be aware that you’re not going to get the best,
  fastest support experience without paying up.
* We do low, medium, and high quality transcodings for each video we
  serve at Pathwright. Our lower quality encoding is smaller (in terms
  of dimensions) than the medium and high quality encodings. With
  media-nommer and ffmpeg, we were able to specify a fixed width and
  let ffmpeg determine the height (while preserving aspect ratio). The
  Amazon Transcoder currently requires height **and** width for each
  preset, if you want to specify a dimension. Given that our master
  video files are all kinds of dimensions and aspect ratios, this is a
  non-starter for us.
* If you submit an encoding job with an output S3 key name that already
  exists, the job fails. While you do open yourself up to some issues
  in doing so, we would appreciate the ability to say “I want to
  over-write existing files in the output bucket”. There is probably a
  technical reason for this, but I think this fails the practicality
  test. A solution can and should be found to allow this.
* Because of the aforementioned poor support, I still don’t have a good
  answer to this, but it doesn’t appear that you can do two-pass
  encodings. This is a bummer for us, as we’ve been able to get some
  great compression and quality doing this.

Overall verdict
---------------

For Pathwright, the Amazon Transcoder isn’t capable enough to get the
nod just yet. However, the foundation that has been laid is very solid.
The encodings themselves execute quickly, and it’s great not having to
worry about the state of your own in-house encoding infrastructure.

The prices are very fair, and are a large savings over Zencoder and
Encoding.com at the lower to moderate volumes. The price advantage does
taper off as your scale gets very large, and those two services do offer
a lot more capabilities. If your needs are basic, Amazon Transcoder is
likely to be cheaper and “good enough” for you. If you need live
streaming, close captioning, or anything more elaborate, shell out and
go with a more full-featured service.

Once some of the gaping feature gaps are filled and the platform has
time to mature and stabilize, this could be a good service. If the
customer support improves with the features, this could be an excellent service.

**Verdict: Wait and see, but so far, so good.**
