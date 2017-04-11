# HOW TO use this ?
# from setuptools import sandbox
# sandbox.run_setup('setup.py', ['install'])

import os
import subprocess

# e = os.environ.copy()
#e.update({'PYTHONPATH': '/home/alexv/PycharmProjects/foo:' + e.get('PYTHONPATH', '')})
subprocess.check_call(['python', 'setup.py', 'develop'])  # , env=e)
