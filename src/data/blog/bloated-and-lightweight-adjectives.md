---
author: Greg Taylor
pubDatetime: 2014-04-18T00:01:00+00:00
modDatetime:
title: Oft-misused adjectives: Bloated and Lightweight
slug: bloated-and-lightweight-adjectives
featured: false
draft: false
tags: ["Cloud"]
description: ""
---

In software development, we like to re-purpose everyday adjectives. We’llcall a project “unstable”, or “mature”. Maybe we give a nod where it’s due
and say a piece of software is “elegant”. For the most part, this works pretty
well. However, I’m going to take a moment to rant about two
that I see constantly misused:

* Bloated
* Lightweight

Every time I see either of these used, I ignore what follows. There are cases
where these two adjectives make sense, but I argue that these are few and
far between. Some of my hangups may be completely irrational, so take this mostly
as a rant, because who doesn’t like a good rant?

Let’s started with “bloated”.

Bloated
-------

The Dictionary.com definition:

**bloat·ed** [bloh-tid] adjective

1. swollen; puffed up; overlarge.
2. excessively vain; conceited.
3. excessively fat; obese.

Applied in the context of software, this is often used to describe a project
that is larger than it needs to be. It is almost always used as a derogatory
term, used to describe something overly complex. However, in most cases
this term is a too vague and non-specific to be of any use. How “large” should
the project be? What defines “large”? If it were stripped down, would it still
be useful to the same audience? Is it really a problem that you aren’t using
all of the bells and whistles in a module?

When you find yourself considering using “bloated”, ask yourself to more
specifically define your grievances. If the software/library/module
is a sprawling, badly organized mess, you probably want something like “sloppy”
or “tangled”. If you are having a hard time wrapping your head around the basic
usage of said software, maybe you’re looking for “complex” or
“ergonomically challenged”. These point to more specific issues.

“Bloated” can often appear when a developer is having a hard time understanding
a piece of software. Perhaps the real problem is bad documentation, but the
dev may instead just call said software “bloated” and move on.
I also see it used as justification to re-invent the wheel or justify NIH
Syndrome due to a lack of understanding for the original library.

Now that I’ve ranted for a bit, here’s a summary:

* Find a better way to describe your objection. Be more specific!
* Understand that a general-purpose library/module/software product has to
  cover more than just your usage case. If your usage case is specific and narrow,
  you’re more likely to toss around the “B word”.
* It’s OK if you don’t use all of a software product’s features. Disk space
  is cheap.
* If a software product is hard to understand, it may not be “bloated”. It
  may have ergonomic or documentation issues. It could just be messy code.
  Mention these issues instead of referring to the more vague “bloat”.

There are legitimate usage cases for this term, but there is almost always
a better, more specific way to describe why you dislike a piece of software.

Lightweight
-----------

A library being described as “bloated” is almost always followed up with
a recommendation for a more “lightweight” alternative. The Dictionary.com definition:

**light·weight** [lahyt-weyt] adjective

1. light in weight.
2. being lighter in weight, texture, etc., than another item or object of
   identical use, quality, or function: a lightweight topcoat;
   a lightweight alloy for ship construction.

This is probably the more obnoxious of the two terms for me. The intent is to
describe a module as being smaller and more simple than an alternative. The
amusing thing is that the supposed more “lightweight” alternative is of
similar size and complexity to the “bloated” bit. “lightweight” is used to
paint a module in a positive light, opposite of “bloated“‘s negative connotation.

As is the case with “bloated”, lightweight is a cop out for justifying
why something is better. When you find yourself considering the use of “lightweight”:

* Re-visit and re-define your objection to the first library you were
  considering. Is it sloppy? Does the documentation suck? Does the API
  have ergonomic issues? Does it use too much of your system’s resources?
  If so, pick a more descriptive adjective.
* Once you have a concise reason for not liking your first candidate library,
  see if your alternative does things better. If so, specifically mention
  what it does better. Does it have better documentation? Alternative is
  “better documented”. Is the API easier to use? Alternative is subjectively
  “easier to use”. Is the code better organized and of higher quality? Alternative
  is “more elegantly designed”.

“Lightweight” doesn’t tell us much. Amusingly, it is often used by developers
who were looking to re-invent a more “bloated” piece of software by stripping
a ton of features out, pooping out some documentation, then calling it a day.
Said alternative often lacks the community to see much maintenance, and
it often lacks widely used features that its predecessor had.

There are legitimate usage cases for this term, but there is almost always
a better, more specific way to describe why an alternative to something is better.

Summary
-------

In closing, it’s important to remember that open source software is created
and developed by other real humans. They tend to take some amount of pride in their
work. It’s OK to criticize software, it often motivates positive change.
However, it’s important to be specific and fair with criticism. Don’t
cop out when describing what makes you dislike a certain library/module/software
product. Get specific, be fair, and maybe everyone will benefit.
