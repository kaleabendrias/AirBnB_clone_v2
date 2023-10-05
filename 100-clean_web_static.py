#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
import os


env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """ deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    else:
        number += 1
    
    # delete old archives in cersions folder
    with lcd("versions"):
        local("ls -t | tail -n +\
{} | xargs -I {{}} rm -f {{}}".format(number))
    
    # delte old archives in /data/web_static_releases
    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +\
{} | xargs -I {{}} rm -rf {{}}".format(number))

        