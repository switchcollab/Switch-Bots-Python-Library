#!/bin/sh

# This script is used to publish the swibots package to the pip repository.

# This script is part of the swibots package.
rm -rf dist
rm -rf build
mkdir dist
mkdir build
python setup.py sdist bdist_wheel
twine upload dist/*