# Exercise-2018

1. Needed modules:
	
		module load git
		module load gcc/7
		module load java/1.8
		export TMPDIR=/tmp/$USER

* Use project directory as home is small


2. Install Anaconda:

- Download: https://www.anaconda.com/download

		conda install pip
		conda install -c conda-forge jupyterlab
		conda install -c conda-forge pyspark


4. Jupyter

    * Secure configuration:
        http://jupyter-notebook.readthedocs.io/en/stable/config_overview.html
    * Socks proxy: `ssh -fND 4223 coolmuc2`



3. Install Pilot-Streaming:

		git clone https://github.com/radical-cybertools/pilot-streaming.git
		pip install --upgrade .


4. Daten:
	



Howto Slurm:

Show clusters

	 sacctmgr list clusters

Show Info for 1 Cluster

	sinfo --clusters=mpp3

Show Info for default cluster
	sinfo