#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
import os


env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """ deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number + 1)

    # delete old archives in cersions folder
    local("cd versions && ls -t | tail -n +\
{} | xargs -I {{}} rm -f {{}}".format(number))

    # delte old archives in /data/web_static_releases
    run("cd /data/web_static/releases && ls -t | tail -n +\
{} | xargs -I {{}} rm -rf {{}}".format(number))
