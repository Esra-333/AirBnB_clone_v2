#!/usr/bin/python3

import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.mont,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute
                                                         dt.secound)


   if os.path.isdir("versions") is False:
       if local("mkdir -p versions").failed is True:
           return None
   if local("tar -cvzf {} web_static".format(file)).failed is True:
       return None
   return file
