#!/usr/bin/env python

import os, sys
from tempfile import NamedTemporaryFile

os.system("ssh  andre@da killall -9 sshd")
for i in range(16):
    script="""#!/bin/bash
#SBATCH -o jupyter.%j.%N.out
#SBATCH -D .
#SBATCH -J jupyter
#SBATCH --get-user-env
#SBATCH --clusters=ivymuc
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
##SBATCH --cpus-per-task=28
#SBATCH --mail-type=end
#SBATCH --mail-user=andre.luckow@gmail.com
#SBATCH --export=NONE
#SBATCH --time=01:00:00
#SBATCH --reservation=big_data_course
source /etc/profile.d/modules.sh
echo $hostname
source /naslx/projects/pn69si/mnmda001/students/software/anaconda3/bin/activate root
cd /naslx/projects/pn69si/mnmda001/students
ssh -fN -R *:{}:localhost:8888 andre@da
jupyter-lab --no-browser""".format(1730+i)
    print(script)
    fp = NamedTemporaryFile(delete=False)
    fp.write(script.encode())
    fp.flush()
    print(fp.name)
    os.system("sbatch --clusters=ivymuc %s"%fp.name)
    fp.close()
