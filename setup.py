#!/usr/bin/python
# -*- coding: utf-8 -*-

# By Dennis Drescher (sparkycbr at gmail dot com)

# Import modules
import os
from distutils.core                     import setup
from glob                               import glob
from configobj                          import ConfigObj

# Grab some app/system info
projBase                                = os.getcwd()
sysConfig                               = ConfigObj(os.path.join(projBase, 'config', 'system.ini'), encoding='utf-8')
systemName                              = sysConfig['Rapuma']['systemName']
systemAbout                             = sysConfig['Rapuma']['systemAbout']
systemVersion                           = sysConfig['Rapuma']['systemVersion']
daMan                                   = sysConfig['Rapuma']['maintainer']
daMansEmail                             = sysConfig['Rapuma']['maintainerEmail']

datafiles = []
# This sets the path for usr/local/share/rapuma
dataprefix = "share/rapuma"

for subdir in ('doc', 'resource', 'config', 'xetex-64') :
    for (dp, dn, fn) in os.walk(subdir) :
        datafiles.append((os.path.join(dataprefix, dp), [os.path.join(dp, f) for f in fn]))

setup(name = 'rapuma',
        version = systemVersion,
        description = systemName,
        long_description = systemAbout,
        maintainer = daMan,
        maintainer_email = daMansEmail,
        package_dir = {'':'lib'},
        packages = ["rapuma", 'rapuma.core', 'rapuma.group', 'rapuma.manager', 'rapuma.project'],
        scripts = glob("scripts/rapuma*"),
        license = 'GPL',
        data_files = datafiles
     )


