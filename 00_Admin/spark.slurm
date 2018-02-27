#!/bin/bash
mkdir work

#SBATCH -o work/spark%j.%N.out 
#SBATCH -D . 
#SBATCH -J spark
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
cd work
python -m pilot.plugins.spark.bootstrap_spark

