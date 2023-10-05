#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """Clean up old archives."""
    number = int(number)

    if number < 1:
        number = 1

    # Clean local archives
    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        archives_to_delete = local_archives[:-number]
        for archive in archives_to_delete:
            local("rm -f {}".format(archive))

    # Clean remote archives
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr | grep 'web_static_'").split()
        archives_to_delete = remote_archives[:-number]
        for archive in archives_to_delete:
            run("rm -rf {}".format(archive))
