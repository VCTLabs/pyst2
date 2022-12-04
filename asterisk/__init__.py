""" pyst - A set of interfaces and libraries to allow programming of asterisk from python.

The pyst project includes several python modules to assist in programming
asterisk with python:

agi     - python wrapper for agi
agitb   - a module to assist in agi debugging, like cgitb
config  - a module for parsing asterisk config files
manager - a module for interacting with the asterisk manager interface

"""

from . import agi, agitb, config, manager
from ._version import __version__

version = __version__

__all__ = ['agi', 'agitb', 'config', 'manager']
