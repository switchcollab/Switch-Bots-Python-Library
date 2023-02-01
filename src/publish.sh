#!/bin/sh

# This script is used to publish the swibots package to the pip repository.

# This script is part of the swibots package.

python setup.py sdist bdist_wheel
twine upload dist/*