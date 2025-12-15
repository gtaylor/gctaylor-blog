---
author: Greg Taylor
pubDatetime: 2012-06-25T04:50:00+00:00
modDatetime:
title: petfinder-api released
slug: petfinder-api-released
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

tldr; I have released [petfinder-api](http://pypi.python.org/pypi/petfinder/), a Python client to[Petfinder.com](http://www.petfinder.com/)‘s web API. Important links: [Documentation](http://petfinder-api.readthedocs.org/),
[source](https://github.com/gtaylor/petfinder-api). petfinder-api is under the [BSD License](https://github.com/gtaylor/petfinder-api/blob/master/LICENSE).

After months of waiting for things to settle down, Erin and I decided to
spend the time to pick out our long-awaited second dog. Given that we
wanted to rescue a dog, the obvious place to go is [Petfinder](http://www.petfinder.com/).

We set out to find the perfect dog for Erin and I, and filtered down to
what we were looking for. That only left… 36 pages to sort through.
Petfinder’s filtering capabilities are very limited, the result display
lists are somewhat hard to look through, and the whole thing is just
pretty clunky.

Out of frustration (we had been half heartedly looking for months), my
mind had often entertained the thought of trying to do better. Petfinder
generously built in an API to get at their data, and it looked pretty
simple. The problem was, I couldn’t find a packaged, maintained
Petfinder API for Python. So it became my weekend project. This would be
the first step towards making something more useful than Petfinder
(getting on near equal footing as far as data goes).

I may or may not ever actually develop a Petfinder+, but I consider
making it easier for developers to use their data a good cause, and am
proud to announce the release of [petfinder-api](http://pypi.python.org/pypi/petfinder/). It is a very thin
wrapper around their web API, and includes [documentation](http://petfinder-api.readthedocs.org/).

I’d love to hear any feedback, and hope this is useful to someone!
