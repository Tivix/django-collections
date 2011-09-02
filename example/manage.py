#!/usr/bin/env python
from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import os
import sys

#insert the parent folder into the python path so we can access collections
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
head, tail = os.path.split(PROJECT_ROOT)
sys.path.insert(0, head)


import settings

if __name__ == "__main__":
    execute_manager(settings)
