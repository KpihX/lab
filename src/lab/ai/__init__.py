"""KπX-Labs AI utility kit.

Encapsulation rule (mandatory across all __init__.py):
Never break package encapsulation inside __init__.py with cross-module re-exports.
Direct imports in __init__.py are strictly reserved for a submodule sharing the exact
same name as its enclosing package (e.g. from .ai import class_eval inside package ai/),
when its contents must be directly accessible from the package root without sub-import.
"""

from .ai import class_eval
