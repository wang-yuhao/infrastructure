#!/bin/bash
#SBATCH -o work/jupyter.%j.%N.out 
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
##SBATCH --reservation=mpp3-Lehrveranstaltung

source /etc/profile.d/modules.sh

echo $hostname
source /naslx/projects/pn69si/mnmda001/students/software/anaconda3/bin/activate root
cd ..

ssh  andre@da killall -9 sshd
ssh -fN -R *:8080:localhost:8888 andre@da

jupyter-lab --no-browser
