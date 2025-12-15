---
author: Greg Taylor
pubDatetime: 2012-02-29T05:58:00+00:00
modDatetime:
title: txWS example project
slug: txws-example-project
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

I recently got the itch to check up on WebSockets, and tinker with a few ideas I have been tossing around. Some searching around led me to
[txWS](https://github.com/MostAwesomeDude/txWS), which supported a newer version of the spec, and was organized
to my liking. The only problem was, it wasn’t immediately apparent how
to use it without some prior knowledge of Twisted.

Rooting around in the txWS issue tracker, I found an issue complaining
about the lack of a simple example. Someone chimed in with a link to a
[gist by zed](https://gist.github.com/1380305), which contained a very concise and useful sample of how
everything fits together.

I figured I’d take the next step and re-organize it to my liking, stick
some more comments in, and post up a project for me to base my various
tinker projects on. The end result of this is [txWS-example-project](https://github.com/gtaylor/txWS-example-project).

As a result of this mostly being for me, you may or may not like my
particular project structure, but hopefully you can still get the basic
idea of how to use txWS.
