#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['mission_planners/remote.py','scripts/imu_tf_publisher.py','scripts/fault_detector.py'],
)

setup(**d)