#!/bin/bash
#SBATCH -o jupyter.%j.%N.out 
#SBATCH -D .
#SBATCH -J jupyter
#SBATCH --get-user-env 
#SBATCH --clusters=mpp3
#SBATCH --nodes=1-1 
#SBATCH --cpus-per-task=28  
#SBATCH --mail-type=end 
#SBATCH --mail-user=xyz@xyz.de 
#SBATCH --export=NONE 
#SBATCH --time=48:00:00 
##SBATCH --reservation=mpp3-Lehrveranstaltung

source /etc/profile.d/modules.sh

echo $hostname
source $HOME/anaconda2/bin/activate
cd ..
jupyter-lab --no-browser
