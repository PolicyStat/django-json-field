#!/usr/bin/env python
import os
import sys

try:
    import test_project.settings as settings_mod  # Assumed to be in the test_project directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the test_project directory. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

sys.path.insert(0, settings_mod.PROJECT_ROOT)
sys.path.insert(0, settings_mod.PROJECT_ROOT + '/../')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
