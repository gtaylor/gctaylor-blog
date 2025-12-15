---
author: Greg Taylor
pubDatetime: 2011-07-18T00:11:00+00:00
modDatetime:
title: Rabbits for the celery
slug: rabbits-celery
featured: false
draft: false
tags: ["Python", "Linux", "Django"]
description: ""
---

I run an [Arch Linux](http://archlinux.org) desktop as my primary development workstation.We use [celery](http://celeryproject.org/) pretty heavily on some of our Django projects, and I
was working to get my local environment at least somewhat closer to our
production setup, only to find there isn’t a non-AUR package for rabbitmq-server.

Of course you can just download an AUR package, but that’s not nerdy
enough. I managed to get a [GitHub project to act as a pacman
repository](https://github.com/duointeractive/archduo), and will share it here in case anyone else would like to
stay up to date with rabbitmq-server without mucking with the AUR
packages yourselves.

Just to be clear, there is no real benefit to installing from my
repository, other than not having to download PKGBUILDs and mess with
compiling/installing yourself. I just yanked the highest voted
[rabbitmq-server](http://aur.archlinux.org/packages.php?ID=19090) off of AUR and sucked it into a repository.

If there are any other common packages that you use that I might also
use, comment on here and I might be convinced into pulling them in.

Repository: <https://github.com/duointeractive/archduo>
