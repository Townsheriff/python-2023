#! /bin/bash

export CONDA_DEBUG=0

set -e 

ENV_NAME="python-parse-logs"

# install anaconda - https://www.anaconda.com/download

conda config --add channels conda-forge

conda create --name $ENV_NAME python=3.8 --yes --quiet 1> /dev/null
echo "Created python env ${ENV_NAME}"

source ~/anaconda3/etc/profile.d/conda.sh
echo "Conda set for script"

conda activate $ENV_NAME

conda install --file requirements.txt --yes 1> /dev/null

# It sometimes does not install from requirements
conda install tailer
