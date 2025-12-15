---
author: Greg Taylor
pubDatetime: 2020-07-02T23:30:47+00:00
modDatetime:
title: Building FoundationDB on macOS with Homebrew
slug: building-foundationdb-on-macos-with-homebrew
featured: false
draft: false
tags: ["foundationdb", "Mac"]
description: ""
---

In case you need to build [FoundationDB](https://www.foundationdb.org/) on macOS without the upstream-provided Docker build container, here’s how to do it!

Note: These instructions assume that you have [Homebrew](https://brew.sh/) installed under the default /usr/local path. Make sure to update the paths below if you’ve installed somewhere else.

As per the [Compiling from Source](https://github.com/apple/foundationdb#compiling-from-source) section of the FoundationDB README, this build is memory hungry! You may need to “ninja -j1” to reduce the overhead, at the expense of compile time.
