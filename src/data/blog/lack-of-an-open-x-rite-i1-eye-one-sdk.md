---
author: Greg Taylor
pubDatetime: 2008-07-25T19:57:00+00:00
modDatetime:
title: Lack of an open X-Rite i1 (Eye-One) SDK
slug: lack-of-an-open-x-rite-i1-eye-one-sdk
featured: false
draft: false
tags: ["Color Science", "Programming"]
description: ""
---

After doing a lot of work with the X-Rite (formerly Gretagmacbeth) i1(Eye-One) Pro SDK, I’ve started running into strange little quirks with
their close-sourced libraries. The documentation is decent, but severely
lacking in crucial areas such as code examples. Several of the functions
are vaguely defined with no examples whatsoever. To make matters worse,
there is absolutely no developer community since the SDK isn’t publicly available.

So if you’re running on a platform other than Windows or Mac OSX, you’re
generally out of luck. There is a rudimentary set of drivers that an
open source color profiling library has implemented, but it does not
handle many of the features and not nearly as well as the X-Rite SDK.
Fortunately, I’ve been able to at least abstract some of the quirks away
by writing a Python wrapper around their C library, but there are still
some things that would be high on the list for improvement if the
Eye-One SDK were publicly available.

It is a pity this stuff is kept under such tight wraps. I’m not sure if
they realize, but X-Rite could be promoting a flourishing community of
developers rather than squashing any code examples on the net and not
even hosting a rudimentary communication device such as a mailing list
for people to share their work and ask questions. Perhaps they fear the
software people would create if the tools were better documented and
help was available. Maybe it’d challenge their monopoly and it’d be a
bad thing.

Who knows, I guess.
