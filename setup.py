#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    setup.py
    ~~~~~~~~

    installation script

    :copyright: (c) 2013-2015 by Jauhien Piatlicki
    :license: GPL-2, see LICENSE for more details.
"""

from distutils.core import setup

setup(name          = 'gs-elpa',
      version       = '0.2',
      description   = 'g-sorcery backend for elisp packages',
      author        = 'Jauhien Piatlicki',
      author_email  = 'jauhien@gentoo.org',
      packages      = ['gs_elpa'],
      package_data  = {'gs_elpa': ['data/*']},
      scripts       = ['bin/gs-elpa'],
      data_files    = [('/etc/g-sorcery/', ['gs-elpa.json']),
                       ('/etc/layman/overlays/', ['gs-elpa-overlays.xml'])],
      license       = 'GPL-2',
      )
