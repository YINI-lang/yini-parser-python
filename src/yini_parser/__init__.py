# src/yini_parser/__init__.py
"""Public API for the yini_parser package."""

from .api import YiniParseError, load, loads

"""
So users can write:
from yini_parser import load, loads, YiniParseError

Instead:
from yini_parser.api import load, loads, YiniParseError
"""

__all__ = ["YiniParseError", "load", "loads"]
