#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
from datetime import datetime

env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """fabric method"""
    if int(number) < 0:
        return

    archives = sorted(run("ls -1t versions").splitlines())

    # Remove archives to keep
    keep = archives[-int(number):]
    archives = archives[:-int(number)]

    if len(archives) == 0:
        return

    for archive in archives:
        run("rm versions/{}".format(archive))

    # Delete on web servers
    with cd("/data/web_static/releases"):
        run("ls -1t . | tail -n +{} | xargs rm -rf".format(len(keep) + 1))
