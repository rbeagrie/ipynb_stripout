#!/usr/bin/env python
"""strip outputs from an IPython Notebook

This does mostly the same thing as the `Clear All Output` command in the notebook UI.

Adapted from rom https://gist.github.com/minrk/6176788 to work with
git filter driver
"""
import sys

#You may need to do this for your script to work with GitX or Tower:
#sys.path.append("/Users/chris/anaconda/envs/conda/lib/python2.7/site-packages")

from nbformat import v4

def strip_output(nb):
    """strip the outputs from a notebook object"""
    for cell in nb.cells:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = 0
    return nb

def do_stripping():
    nb = v4.reads(sys.stdin.read())
    nb = strip_output(nb)
    sys.stdout.write(v4.writes(nb))
