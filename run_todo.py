#!/usr/bin/env python

from subprocess import run
from pathlib import Path
from sys import argv, platform

if platform == 'win32':
    run(f"echo hello",shell=True, check=True)
    # run(f"cmake --build --preset default && ",shell=True, check=True)
else:
    raise Exception('Only on windows for now.')
