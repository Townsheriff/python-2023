#! /bin/sh

set -e

autopep8 main.py --in-place
echo "Linting finished"