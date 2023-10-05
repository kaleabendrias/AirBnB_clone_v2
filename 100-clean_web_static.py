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

    with cd('/data/web_static/releases'):
        # List archives on the remote server
        archives = run('ls -1').split()

        # Filter archives that start with 'web_static_'
        archives = [archive for archive in archives
                    if archive.startswith('web_static_')]

        # Sort archives by modification time (newest first)
        archives.sort(reverse=True)

        # Keep only the most recent `number` archives
        archives_to_delete = archives[number:]

        # Delete the outdated archives
        for archive in archives_to_delete:
            sudo('rm -rf {}'.format(archive))

    with lcd('versions'):
        # List local archives
        local_archives = local('ls -1', capture=True).split()

        # Keep only the most recent `number` local archives
        if number < len(local_archives):
            local_archives_to_delete = local_archives[number:]
            for archive in local_archives_to_delete:
                local('rm -f {}'.format(archive))
