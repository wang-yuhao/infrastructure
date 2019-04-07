#!/usr/bin/env python

import os, sys

start=3
end=22
prefix="mnmda"
directory="/home/hpc/ug201/di57hah/project/students" 
directory=os.path.join(os.environ["WORK"], "students")

for i in range(start,end):
    os.makedirs(os.path.join(directory, "mnmda%03d"%i))

