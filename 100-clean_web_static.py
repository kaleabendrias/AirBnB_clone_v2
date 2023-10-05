#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
from datetime import datetime

env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """fabric method"""
    number = int(number)
    if number == 0:
        number = 1
    local("cd versions && ls -t | head -n -{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | head -n -{} | xargs rm -fr".format(path, number))