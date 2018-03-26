#!/bin/bash
#SBATCH -o work/jupyter.%j.%N.out 
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
source $HOME/anaconda2/bin/activate root
cd ..

ssh  vlsshforward@data-analytics.dyndns.lrz.de killall -9 sshd
ssh -fN -R *:8080:localhost:8888 vlsshforward@data-analytics.dyndns.lrz.de

jupyter-lab --no-browser
