#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *


def do_clean(number=0):
    """ deletes out-of-date archives"""
    