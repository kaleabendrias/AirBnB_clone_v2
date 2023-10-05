#!/usr/bin/python3
"""fabfile to gnerate a tar file of web_static"""
from fabric.api import local
from time import strftime
from datetime import datetime
import os


def do_pack():
    """# creating a tar file"""
    try:
        now = datetime.now()
        local("mkdir -p versions/")
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + time_format + ".tgz"
        archive_path = os.path.join("versions", archive_name)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None
