#! /bin/sh

conda list | grep autopep8 >> /dev/null

if [ $? -ne 0 ]; then
  conda install -c conda-forge autopep8 --yes
fi

set -e

autopep8 main.py --in-place
echo "Linting finished"