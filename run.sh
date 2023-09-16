#! /bin/bash

export CONDA_DEBUG=0

set -e 

# install anaconda - https://www.anaconda.com/download

conda create --name python-3-8 python=3.8 --yes --quiet 1> /dev/null
echo "Created python env for 3.8"

source ~/anaconda3/etc/profile.d/conda.sh
echo "Conda set for script"

conda activate python-3-8
conda install --file requirements.txt --yes 1> /dev/null
python main.py
