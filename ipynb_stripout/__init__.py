import sys

if sys.version[0] > 2:
    from ipynb_stripout_v3 import do_stripping
else:
    from ipynb_stripout import do_stripping
