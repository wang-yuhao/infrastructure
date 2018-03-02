#!/bin/bash

#SBATCH -o work/spark%j.%N.out 
#SBATCH -D . 
#SBATCH -J spark
#SBATCH --get-user-env 
#SBATCH --clusters=mpp3
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=64
#SBATCH --mail-type=end 
#SBATCH --mail-user=andre.luckow@gmail.com
#SBATCH --export=NONE 
#SBATCH --time=48:00:00 

source /etc/profile.d/modules.sh

mkdir work
echo $hostname
source $HOME/anaconda2/bin/activate
cd work
python -m pilot.plugins.spark.bootstrap_spark

