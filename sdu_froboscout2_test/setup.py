from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['mission/keyboard_mission_node.py',
  'mission/wiimote_mission_node.py',
  'navigation/waypoint_navigation_node.py',
  'monitor/lighthouse_node.py'],)
setup(**d)

