---
author: Greg Taylor
pubDatetime: 2025-12-14T21:48:28-08:00
modDatetime:
title: Squarespace to Astro script
slug: squarespace-to-astro-script
featured: false
draft: false
tags: ["Python", "How To"]
description: A quick and dirty script to convert Squarespace blog exports to Astro markdown files.
---

In case this is helpful, [here](https://gist.github.com/gtaylor/bdccbd2143c445819222c4ed243e04ee) is a quick and dirty script for converting Squarespace blog [exports](https://support.squarespace.com/hc/en-us/articles/205814028-Importing-and-exporting-content) to [Astro](https://astro.build/)-compatible Markdown files. Some things to watch out for:

1. You'll need to run this via [uv run](https://docs.astral.sh/uv/guides/scripts/).
1. Since this was mostly for me, I hardcoded the configs in global variables. Yuck!
1. The script doesn't migrate images or clean up unwanted tags. You may need to add these on your own, depending on your situation.

I can't offer any support for this gist but hope this will serve as useful prior art to others doing similar migrations.
