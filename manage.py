#!/usr/bin/env python
import os
import sys
这下怎么办
commit 1
commit 3
commit 4
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
