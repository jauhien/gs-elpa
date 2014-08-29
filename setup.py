#!/usr/bin/env python

from distutils.core import setup

setup(name          = 'gs-elpa',
      version       = '0.1.1',
      description   = 'g-sorcery backend for elisp packages',
      author        = 'Jauhien Piatlicki',
      author_email  = 'jauhien@gentoo.org',
      packages      = ['gs_elpa'],
      package_data  = {'gs_elpa': ['data/*']},
      scripts       = ['bin/gs-elpa'],
      data_files    = [('/etc/g-sorcery/', ['gs-elpa.json']),
                       ('/etc/layman/overlays/', ['gs-elpa-overlays.xml'])],
      license       = 'GPL',
      )
