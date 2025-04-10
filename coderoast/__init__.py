"""
CodeRoast - A Python library that insults programmers when their code throws errors.
"""

__version__ = "0.2.0"
__author__ = "Not a Real Programmer"
__email__ = "notarealprogrammer010@gmail.com"
__license__ = "MIT"

from .core import CodeRoast
from .insults import RoastLevel

__all__ = ['CodeRoast', 'RoastLevel']