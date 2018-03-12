1. Anaconda Install

    * Download: https://www.anaconda.com/download

            conda install pip
            conda install -c conda-forge jupyterlab
            conda install -c conda-forge pyspark
            conda install pytorch-cpu torchvision -c pytorch
            conda install -c conda-forge keras
            
            


4. Jupyter

    * Secure configuration:
        * http://jupyter-notebook.readthedocs.io/en/stable/config_overview.html
    * SSL certificate:
        * openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mykey.key -out mycert.pem
    
    * Socks proxy: `ssh -fND 4223 coolmuc2`
    



3. Install Pilot-Streaming:

		
    git clone https://github.com/radical-cybertools/pilot-streaming.git
    cd pilot-streaming
    pip install --upgrade .
    
    
2. Start Clusters