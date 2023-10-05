#!/usr/bin/python3
""" a Fabric script that distributes an archive to your web servers"""
from fabfile.api import *
from os import path


env.hosts = ['35.175.126.161', '54.164.52.24']
env.user = "ubuntu"
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """deploys the archives to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        # uploading the archive
        put(archive_path, "/tmp/")
        print('here')

        # uncompress the archive
        parts = archive_path.split('_')
        time_stamp = parts[2].split(".")[0]
        run(f"sudo rm -rf /data/web_static/releases/web_static_{time_stamp}")
        run(f"sudo mkdir -p /data/web_static/releases/web_static_{time_stamp}")
        run(f"sudo tar -xvf /tmp/web_static_{time_stamp}.tgz -C /data/\
web_static/releases/web_static_{time_stamp}")

        # delete the archive from web_server
        run(f"sudo rm -rf /tmp/web_static_{time_stamp}.tgz")

        # delete the symbolic link
        run("sudo rm -rf /data/web_static/current")

        # create a new symblolic link
        run(f"sudo ln -sf /data/web_static/releases/\
web_static_{time_stamp} /data/web_static/current")

        return True
    except Exception as e:
        return False
