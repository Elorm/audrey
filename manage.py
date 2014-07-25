#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "audrey.settings")

    from django.core.management import execute_from_command_line
    import audrey.startup as startup
    try:
    	startup.run()
    except:
    	pass

    execute_from_command_line(sys.argv)
