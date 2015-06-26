# -*- coding: cp949 -*-
from distutils.core import setup
import py2exe

excludes = [
    "pywin",
    "pywin.debugger",
    "pywin.debugger.dbgcon",
    "pywin.dialogs",
    "pywin.dialogs.list",
    "win32com.server",
]

includes = [
    #files to include
]

options = {
    'bundle_files': 1,                 # create singlefile exe
    'compressed'  : 1,                 # compress the library archive
    'optimize'    : 2,
    'excludes'    : excludes,
    'includes'    : includes,
    'dll_excludes': ["w9xpopen.exe"],   # we don't need this
    'dist_dir'    : './dist'
}

setup(
    # information
    name = "CCleaner Auto Updater",
    version = "0.1",
    description = "CCleaner Auto Updater 0.1",
    author="Bums Kim",
    author_email="bskim45@gmail.com",
    url="http://bsk.im",

    # packaging
    options = {"py2exe": options},
    zipfile = None,                    # append zip-archive to the executable

    console = ['CCleanerAutoUpdate.py']
)
