---
author: Greg Taylor
pubDatetime: 2011-07-20T17:46:00+00:00
modDatetime:
title: Exocet makes code reloading easy
slug: exocet-makes-code-reloading-easy
featured: false
draft: false
tags: ["Mud", "Python", "Programming"]
description: ""
---

One of the big philosophical “pillars” I’ve been building my [tinkerPython MUD](https://github.com/gtaylor/dott) on is that cold restarts (restart the process, clients are
disconnected) should be exceedingly rare. Code re-loading in Python can
be challenging, but Allen Short has nailed it with his [Exocet](http://washort.twistedmatrix.com/2011/01/introducing-exocet.html) module.

The coolest part for me (as it pertains to my game) is as follows:

*“Exocet is a new way to load Python modules. It separates the act of
naming a dependency from the act of creating a module object. As a
result, more than one instance of a module can be created from the
same source file.”*

As a result of this, we can deal with Python modules as objects, and can
easily replace them. This is how it ends up looking for me (lots of
things removed for the sake of brevity):

```
import exocet
# Load the general commands module, stuff it in a variable.
general_cmds = exocet.loadNamed(
   'src.game.commands.general',
   exocet.pep302Mapper
)
# Add a command to the command table.
self.add_command(general_cmds.CmdLook())
```

This is an excerpt from my game’s [global command table](https://github.com/gtaylor/dott/blob/master/src/game/commands/global_cmdtable.py). The general
command module is loaded by exocet instead of Python’s regular import
statement. Since we’ve tossed the module reference in a variable, the
normal rules of Python garbage collection apply.

While my game does this a little differently, running the line that
populates *general\_cmds* again would mean that the old general command
module’s reference count would drop to zero, hence it would be garbage
collected. In its place, you have the newly loaded general commands
module with any new code updates. Here is all I’d need to do to re-load
the general commands module after some modifications:

```
import exocet
# Re-load the general commands module, replacing the old one.    general_cmds = exocet.loadNamed(
   'src.game.commands.general',
   exocet.pep302Mapper
)
```

Some disclaimers
----------------

Of course there had to be a catch, right? I’m still learning how to best
use this, but here are a few pointers:

* Your Exocet-based imports will probably always look strange to you,
  because they are. However, the power you get from them is well worth
  the “different” look to them. This is a pretty silly point, but I am
  pretty silly about code cosmetics.
* Be careful about storing references to exocet-loaded modules. If you
  reference an exocet module from other modules/classes, you may find
  yourself in a situation where the old module’s reference count never
  drops to zero, and it isn’t garbage collected. I get around this by
  using properties to replace things that were previous instance
  attributes. I probably did a bad job explaining this, sorry!
* Exocet is still in development. It is only available on
  [Launchpad](https://launchpad.net/exocet) (sadface). However, some pip+bzr magic can make that
  less of a problem.
* Documentation is limited to a [series of blog posts](http://washort.twistedmatrix.com/search/label/exocet) by the author.
  They are pretty useful, but you’ll have to wade through them if
  you’re looking for something.
