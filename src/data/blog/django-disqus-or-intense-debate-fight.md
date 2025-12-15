---
author: Greg Taylor
pubDatetime: 2010-02-17T19:43:00+00:00
modDatetime:
title: Django + Disqus or Intense Debate… Fight!
slug: django-disqus-or-intense-debate-fight
featured: false
draft: false
tags: ["Programming", "Django"]
description: ""
---

**Update (3/4/2012): Since this article was posted in early 2010, Disqushas continued to improve. IntenseDebate has made some progress, but
hasn’t been able to keep up with Disqus as far as continued development
goes. As of this week, `I have switched to Disqus`\_. This article is out
of date (by a few years), so treat it as an artifact from the past.**

As most Django blogs seem to be going with [Disqus](http://disqus.com/) these days, I set
out to try it for myself. The install was simple enough, but Disqus was
unable to reach my production site (the one you’re looking at) most of
the time. Every once in a while, it’d decide that it felt like working,
which left me with the normal Disqus comment box. Great.

I tested my shiny new comments by leaving one, and all was good… Until
I browsed to another one of my posts and found my comment from an
earlier post repeated there. Lots of diving through configuration,
submitting a help request, and double checking everything many times
lead to nothing. I even tried arthurk’s excellent [django-disqus](http://github.com/arthurk/django-disqus)
Django app with the same result.

So I debated… Intensely
-----------------------

Having ended up pretty frustrated, I decided to give [Intense Debate](http://intensedebate.com/) a
shot. Installation was very simple, the instructions were clear like
Disqus’. However, when the moment of truth came to test and render
comments, Intense Debate *worked*.

Not only that, but Intense Debate’s configuration and settings dialogs
are much cleaner, polished, and respond in ways that are predictable.
With Disqus, I found it very frustrating that I was unable to
change/save certain fields (Time Zone is one that sticks out to me)
without doing goofy things like Tabbing and hitting Enter.

For now, Intense Debate is looking pretty good, and offers pretty much
the same functionality. I realize that most of the Django userbase seems
to be moving towards Disqus, but if you haven’t checked out Intense
Debate, it’s definitely worthwhile now. I get the sense that last year
the feature gap was much wider in Disqus’ favor, but looks to have
closed somewhat.

Category Winners
----------------

A Disclaimer: I have no particular allegiance towards either of these
services, I just wanted comments for my Django blog. I still don’t really
care either way which is “better”, but figured I’d share my experience
with other Django bloggers out there. For those that are considering
Disqus, arthurk gets major props for his [django-disqus](http://github.com/arthurk/django-disqus) project.

* **Installation:** Intense Debate. Even if Disqus worked for me as
  intended, Intense Debate’s installation was a little easier for a
  custom install. This is only by a small margin, since it’s pretty
  much the same thing for both, but ID required less copy/pasting.
* **Appearance:** Disqus by a narrow margin. I like the comment display
  a little bit better.
* **Administration:** Intense Debate. Some will disagree here, but I
  like the cleaner, faster, minimlistic look.
* **Page Loading:** Disqus by a small margin. I think some of this may
  be in rendering, not net time. There’s just a little bit more page
  movement on loading in ID.
