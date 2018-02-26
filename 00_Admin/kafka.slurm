#!/bin/bash
#SBATCH -o kafka.%j.%N.out 
#SBATCH -D . 
#SBATCH -J kafka
#SBATCH --get-user-env 
#SBATCH --clusters=mpp3
#SBATCH --nodes=1-1 
#SBATCH --cpus-per-task=56 
#SBATCH --mail-type=end 
#SBATCH --mail-user=xyz@xyz.de 
#SBATCH --export=NONE 
#SBATCH --time=2:00:00 
source /etc/profile.d/modules.sh

echo $hostname

source $HOME/anaconda2/bin/activate
mkdir work
cd work
