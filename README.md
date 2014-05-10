This is [g-sorcery](https://github.com/jauhien/g-sorcery) backend for elisp packages.


Installation and using
======================

Installation: in progress (use dev-portage/g-sorcery-9999, at the moment it has bundled backends).

There are two ways of using **gs-elpa**:

* use it with **layman**

In this case all you need to do is install **layman-9999** and **g-sorcery**.
Then you should just run `layman -L` as
root and find an overlay you want. Type of overlay will be
displayed as *g-sorcery*. Then you add this overlay as
usual. It's all you need to do and it's the recommended way of
using **g-sorcery**.

Using **g-sorcery** with layman you can populate overlay only with packages you want.
To do so you should add a section named BACKEND (BACKEND here is the name of backend used for
your repo). In this section you can add entries named REPO_packages (REPO here is the name
of repository you want to add) which are space separated lists of packages you need. ebuilds for
dependencies will be generated automatically if backend supports this possibility.

Note, that some overlays may depend on other overlays, in this case you'll need to add those
dependencies first.


* use it as stand-alone tool

In this case you should create an overlay (see **portage** documentation), sync it and populate
it with one or more ebuilds. Then ebuilds could be installed by emerge or by **gs-elpa** tool.

**Using gs-elpa with layman**

Execute

**layman -L**

Find there an overlay you need (there are
3 gs-elpa overlays currently: gnu-elpa, marmalade and melpa).
Add, e.g.

**layman -a gnu-elpa -a marmalade**

Emerge any package from it, e.g.

**emerge -va clojure-mode**

To generate only ebuilds we need such a */etc/g-sorcery/g-sorcery.cfg* file can be used:

```
[main]
package_manager=portage

[gs-elpa]
marmalade_packages = clojure-mode clojurescript-mode
```


**Generating user ebuilds in user overlay**

Create new user overlay. Run

**gs-elpa -o** *OVERLAY_DIRECTORY* **-r gnu-elpa** **sync**

List packages:

**gs-elpa -o** *OVERLAY_DIRECTORY* **-r gnu-elpa** **list**

Install any package you want:

**gs-elpa -o** *OVERLAY_DIRECTORY* **-r gnu-elpa** **install** *PACKAGE*

Repositories you can use are gnu-elpa, marmalade and melpa. You can use them
all in one overlay. Note, that if you call **generate-tree** command your overlay
will be wiped and overlay tree for a given repository will be generated. Be careful!

See man page of **gs-elpa** for further information.
