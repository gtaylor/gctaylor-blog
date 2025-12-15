---
author: Greg Taylor
pubDatetime: 2015-02-05T22:31:00+00:00
modDatetime:
title: python-fedex 1.1.0 released
slug: python-fedex-110-released
featured: false
draft: false
tags: ["Python", "Programming"]
description: ""
---

I am pleased (and somewhat embarrassed) to release [python-fedex](https://pypi.python.org/pypi/fedex/) 1.1.0!Pleased in that these changes have been patiently waiting for PyPi for a few
years now, embarrassed in that I’ve let the project sit since I stopped
using it more than five years ago. Let’s re-visit that after we talk
about the changes:

* A quick PEP8 pass on most of the codebase. Yucky. (gtaylor)
* Changing recommended install method to use pip + PyPi. (radlws)
* Updated rate\_request and freight\_rate\_request examples for WSDL v16
  compatibility. (foxxyz)
* Updated rate service WSDL from v8 to v16. (foxxyz)
* Added a freight rate request example (mwcbrent)
* Bump ShipService WSDL to v13. (mwcbrent)
* Update rate example to show multiple ServiceTypes. (danielatdattrixdotcom)

If anyone who actively uses python-fedex would like to take over
maintainership of the project, please get in touch. I have a super hard time
getting psyched up about playing with these FedEx SOAP services for funzies.

A few of the things that need doing, which my younger self skimped on:

* The module is in bad need of unit and integration tests. The FedEx WSDLs
  change periodically, and it’s not always in a backwards-compatible manner.
  The [examples](https://github.com/gtaylor/python-fedex/tree/master/examples) we already have would be a good starting point.
* The label certification stuff should be cleaned up and checked over. The
  process still exists, but it may be different now.

If any of this sounds riveting (or you have other ideas of your own), please
let me know and we can figure something out.

For the rest of you, enjoy python-fedex 1.1.0, in “development” for two and a half years!
