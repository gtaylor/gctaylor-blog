---
author: Greg Taylor
pubDatetime: 2011-05-23T20:10:00+00:00
modDatetime:
title: A word of warning about 1and1.com
slug: word-warning-about-1and1com
featured: false
draft: false
tags: ["General"]
description: ""
---

After dealing with them while working on a client’s website, I can’t, ingood conscience, ever recommend 1and1.com as a domain registrar or DNS
host. Creating, updating, and re-naming CNAMEs and A entries take an
extremely long time, with some users complaining of times over 72 hours.
This is not taking into account propagation time at all, this is just
how long it takes for them to update their own DNS entries on their DNS servers.

We are going on a few hours for my client, but even that is absurd for
just updating an entry. Hopefully once we get to the point where DNS
propagation is happening, it’ll move quickly.

Furthermore, you’re limited to 5 sub-domains, which is an effort to rope
you into one of their more expensive services. You also can’t do
wildcard subdomains.

**tldr: Do not use 1and1.com if you are impatient or on a tight
deadline. CNAME/Host entry updates take anywhere from hours to days,
minus propagation time. They also artificially limit you to 5
sub-domains, and no wildcards at all.**
