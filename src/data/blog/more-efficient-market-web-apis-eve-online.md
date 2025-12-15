---
author: Greg Taylor
pubDatetime: 2012-03-11T06:42:00+00:00
modDatetime:
title: More efficient market web APIs for EVE Online
slug: more-efficient-market-web-apis-eve-online
featured: false
draft: false
tags: ["Cloud", "Gaming", "Programming"]
description: ""
---

There are a handful of market data sites (EVE-Central, Eve Marketeers,Eve Marketdata) out there now, each with their own developer APIs. All
but EVE-Central are relatively new sites, and most seem to suffer from
the occasional, or permanent, sluggishness. It doesn’t appear to be for
lack of hardware, I know several of these sites are running on some
pretty good metal. There appears to be a combination of duties
(accepting incoming data, serving the website, serving the developer
APIs) that really slows the sites down, along with their respective
developer-exposed web APIs. Let’s muse on a cheap, sturdy way to
architect around this somewhat.

For the sake of discussion, I’ll just concern myself with the
web-exposed developer APIs in this post. These are open-to-the-public
services that let other applications grab the market site’s data at
will. This is often done with high frequency, and high volume. From what
I can tell, some of these sites serve their APIs from their primary app
server, which is where the rest of the general web traffic goes through.
In some cases, the same process that serves the site and the developer
API may also accept incoming market data.

Wouldn’t it be nice if we could shove that API traffic off somewhere
else? That would mean sluggishness on the website wouldn’t mean
sluggishness in the API, and vice-versa. For market sites with tons of
API users, this could free up resources for other things. Let’s see
where we can go with this…

The APIs are relatively simple
------------------------------

The good news here is that the APIs on all three sites are relatively
simple. To get the price for an item in a certain region, you just pass
in the region and the item ID. A “recently updated” query may not
require any parameters at all. For the most part, our input is going to
be small, and dictated by EVE’s identifiers for various things (items,
regions, characters).

Here’s what we know
-------------------

* We need a relatively small core set of capabilities for developers to
  find our service useful. Price by region being the biggest.
* We don’t want to have to serve the API requests ourselves, since that
  is boring.
* We’re probably already doing some processing and aggregation of
  incoming data.

Here’s what we can do
---------------------

* Create a daemon whose only purpose is to accept incoming market data
  from the uploaders. This gets queued and pumped into another process
  that does validation, statistical aggregation, and saves such things
  to a DB.
* Based on what new data came in, the process uploads JSON documents to
  Amazon S3, to paths that mimic the current developer APIs (IE: /region/12345/item/123556/).
* External developers can then form the URLs much like they already do,
  hitting S3 instead of your servers.
* Your API is now infinitely scalable, and pretty much impossible to
  bring down under load.
* Access can be left public, or restricted by S3 keys or signed URLs.
* If you are wanting to be self-sufficient, you could even make
  developers pay for the bandwidth they use with Amazon DevPay. Given
  that a few other sites offer free APIs, this may no go over well, though.

Caveats
-------

* You will need to keep track of how long it’s been since various S3
  keys were updated. It may not make sense to always upload the new
  data as it comes in for super active items. You can afford to wait a
  minute or two between updates for very active item+region combos.
* Data transfer into S3 is free, but the bandwidth on your market data
  upload accepter machine may not be.
* You will be uploading to S3 pretty constantly.

Reference Implementation?
-------------------------

I briefly debated whether to attempt to write a reference implementation
for this, but it looks like the state of market uploaders is pretty bad
right now. There’s Contribtastic, but it appears to be very much
centered on EVE-Central. There’s also a Unified Uploader, but it’s
closed-source and Windows-only.

We’ll re-visit this idea if the uploader scene changes.
