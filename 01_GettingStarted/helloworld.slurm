#!/bin/bash
#SBATCH -o myjob.%j.%N.out 
#SBATCH -D .
#SBATCH -J hello
#SBATCH --get-user-env 
#SBATCH --clusters=mpp2
#SBATCH --nodes=1-1 
#SBATCH --cpus-per-task=28 
#SBATCH --mail-type=end 
#SBATCH --mail-user=xyz@xyz.de 
#SBATCH --export=NONE 
#SBATCH --time=08:00:00 
source /etc/profile.d/modules.sh

export OMP_NUM_THREADS=28 

echo $hostname