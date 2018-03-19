#!/bin/bash
mkdir work

#SBATCH -o work/kafka.%j.%N.out 
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
rm -rf /naslx/projects/ug201/di57hah/exercise-2018/00_Admin/work/config/

source /naslx/projects/ug201/di57hah/anaconda2/bin/activate root 
cd work
python -m pilot.plugins.kafka.bootstrap_kafka

