from setuptools import setup

setup(
    name = "ipynb_stripout",
    packages=['ipynb_stripout'],
    entry_points = {
                    'console_scripts': [
                        'ipynb_stripout = ipynb_stripout:do_stripping',
                    ]
                   },
)
