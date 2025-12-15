---
author: Greg Taylor
pubDatetime: 2011-04-13T16:45:00+00:00
modDatetime:
title: Amazon AWS S3 and Setting Response Headers
slug: amazon-aws-s3-and-setting-response-headers
featured: false
draft: false
tags: ["AWS"]
description: ""
---

One of the previously annoying limitations of Amazon S3 was that youcould not specify things like Content-Disposition on a per-request
basis. If we use an MP3 as an example, if you uploaded it without a
Content-Disposition header set, viewing it in a browser via the S3 URL
would likely have your browser playing it rather than downloading. This
behavior varies based on browser, but the big point is that it lead to
inconsistency and confused some less technical users (“What do you mean
I need to Right-Click then Save As?”).

Response Headers over GET to the Rescue!
----------------------------------------

This is recent, but breaking news. Googling around, it seems like this
went largely unnoticed by many, so I’ll bring it up again here. You can
now specify headers for GET requests for keys/objects as URL parameters.
The response from S3 will have your provided headers instead of whatever
was set at the time of upload (or not at all).

See their [announcement forum post](https://forums.aws.amazon.com/ann.jspa?annID=884) for more technical details. As a
general note, boto, my weapon of choice for stuff like this, does not
support this yet. We’re [working on that](https://github.com/boto/boto/issues/163), though.
