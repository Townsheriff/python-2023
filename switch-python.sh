#! /bin/bash

set -e 

# install anaconda - https://www.anaconda.com/download

conda create --name python-3-8 python=3.8 --yes --quiet 1> /dev/null
echo "Created python env for 3.8"

conda create --name python-2-7 python=2.7 --yes --quiet 1> /dev/null
echo "Created python env for 2.7"


source ~/anaconda3/etc/profile.d/conda.sh
echo "Conda set for script"

conda activate python-3-8
python --version

conda activate python-2-7
python --version

