#!/usr/bin/python3
"""a Fabric script"""
from fabric.api import *
from datetime import datetime

env.hosts = ['35.175.126.161', '54.164.52.24']


def do_clean(number=0):
    """fabric method"""
    try:
        number = int(number)
    except ValueError:
        number = 0

    if number < 0:
        number = 0

    # Get a list of all archives in the versions folder
    archives = sorted(run('ls -1 /data/web_static/releases').split('\n'))

    # Keep only the most recent `number` archives
    if number >= len(archives):
        return

    archives_to_delete = archives[:-number]

    # Delete archives in versions folder
    for archive in archives_to_delete:
        run('rm -f /data/web_static/releases/{}'.format(archive))

    # Get a list of all archives in the local versions folder
    local_archives = local('ls -1 versions', capture=True).split('\n')

    # Keep only the most recent `number` local archives
    if number >= len(local_archives):
        return

    local_archives_to_delete = local_archives[:-number]

    # Delete local archives
    for archive in local_archives_to_delete:
        local('sudo rm -f versions/{}'.format(archive))
