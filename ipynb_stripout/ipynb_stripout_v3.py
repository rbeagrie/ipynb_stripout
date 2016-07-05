#!/usr/bin/env python
"""strip outputs from an IPython Notebook

This does mostly the same thing as the `Clear All Output` command in the notebook UI.

Adapted from rom https://gist.github.com/minrk/6176788 to work with
git filter driver
"""
import sys

#You may need to do this for your script to work with GitX or Tower:
#sys.path.append("/Users/chris/anaconda/envs/conda/lib/python2.7/site-packages")

from IPython.nbformat import current

def strip_output(nb):
    """strip the outputs from a notebook object"""
    for cell in nb.worksheets[0].cells:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'prompt_number' in cell:
            cell['prompt_number'] = ""
    return nb

def do_stripping():
    nb = current.read(sys.stdin, 'json')
    nb = strip_output(nb)
    current.write(nb, sys.stdout, 'json')

