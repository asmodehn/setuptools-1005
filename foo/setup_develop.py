# HOW TO use this ?
# from setuptools import sandbox
# sandbox.run_setup('setup.py', ['install'])

import subprocess
subprocess.check_call(['python', 'setup.py', 'develop'])
