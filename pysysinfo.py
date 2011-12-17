#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:" % uname
subprocess.call([uname, uname_arg])
print ""

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace information %s command:" % diskspace
subprocess.call([diskspace, diskspace_arg])