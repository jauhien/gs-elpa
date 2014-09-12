This is [g-sorcery](https://github.com/jauhien/g-sorcery) backend for elisp packages.


Installation
======================

Currently gs-elpa is not keyworded, so [add keywords](https://bitbucket.org/mgorny/flaggie/), then install it:

```
flaggie app-portage/gs-elpa '+**'
```

```
emerge -va gs-elpa
```

Note that it needs layman-9999.


Usage
======================

There are two ways of using **gs-elpa**

** Using gs-elpa with [layman](https://wiki.gentoo.org/wiki/Layman) **

It the the recommend way and I strongly suggest it.

Then you should just run `layman -L` as
root and find an overlay you want. Type of overlay will be
displayed as *g-sorcery*. Then you add this overlay as
usually and emerge packages you want. It's all you need to do. Example:

```
layman -L
layman -a gnu-elpa -a marmalade
emerge -va clojure-mode
```

There are 3 gs-elpa overlays currently: [gnu-elpa](http://elpa.gnu.org/), [marmalade](http://marmalade-repo.org/),
[melpa](http://melpa.milkbox.net/) and [melpa-stable](http://melpa-stable.milkbox.net/).

When using **gs-elpa** with layman you can populate overlay only with packages you want.
To do so you should add a section named gs-elpa to */etc/g-sorcery/g-sorcery.cfg*.
In this section you can add entries named REPO_packages (REPO here is the name
of repository you want to add) which are space separated lists of packages you need. ebuilds for
dependencies will be generated automatically if backend supports this possibility.

```
[main]
package_manager=portage

[gs-elpa]
marmalade_packages = clojure-mode clojurescript-mode
```
Note, that some overlays may depend on other overlays, in this case you'll need to add those
dependencies first (I'd recommend to always add the whole gnu-elpa overlay).


** Using gs-elpa as stand-alone tool **

In this case you should create an overlay (see **portage** documentation), sync it and populate
it with one or more ebuilds. Then ebuilds could be installed by emerge or by **gs-elpa** tool.
This is not the recommended way and may be removed in the future.

Create new user overlay:

```
gs-elpa -o $OVERLAY_DIRECTORY -r gnu-elpa sync
```

List packages:

```
gs-elpa -o $OVERLAY_DIRECTORY -r gnu-elpa list
```

Install any package you want:

```
gs-elpa -o $OVERLAY_DIRECTORY -r gnu-elpa install $PACKAGE
```

Repositories you can use are gnu-elpa, marmalade, melpa and melpa-stable. You can use them
all in one overlay. Note, that if you call **generate-tree** command your overlay
will be wiped and overlay tree for a given repository will be generated. Be careful!

See man page of **gs-elpa** for further information.
