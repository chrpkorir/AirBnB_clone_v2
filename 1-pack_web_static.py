#!/usr/bin/pthon3
"""Fabric script that generates a .tgz archive 
from web_static folder.
"""

from fabric.api import local
from datetime import dateime


@runs_once
def do_pack():
    '''Generates .tgz from web_static folder contents.'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_ststic"
                    .format(path))

    if result.failed:
        return None
    return path
