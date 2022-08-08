from setuptools import setup, Extension, find_packages
from pararun import __version__

setup(
    name='pararun',
    version=__version__,
    packages=['', "pararun", 'test'],
    url='https://github.com/runsheng/pararun',
    license='GPL-2',
    author='runsheng',
    author_email='runsheng.lee@gmail.com',
    description='Generate and run bash scripts for parallel and iterative jobs',

    scripts=['pararun/runpara.py',
             'pararun/runiter.py'],

)