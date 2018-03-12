#!/bin/bash

# run:
# nohup watch_jobs.sh &

while :
do
    squeue -u di57hah | grep jupyter | grep 46:
    check_walltime_jupyter=$?
    number_jupyter_jobs=`squeue -u di57hah | grep jupyter | wc -l`
    echo "Jupyter Job Walltime 46h? ${check_walltime_jupyter} Number Jupyter Jobs: ${number_jupyter_jobs}"
    if [ $check_walltime_jupyter -eq 0 ] && [ $number_jupyter_jobs == "1" ]
    then
        echo "Job ending soon. Queuing new job"
        sbatch jupyter.slurm
    else
        echo "Job NOT ending soon"
    fi
    sleep 3000
done
