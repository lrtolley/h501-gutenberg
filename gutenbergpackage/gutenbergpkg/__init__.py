"""gutenbergpkg

Lightweight helper to load Project Gutenberg tidyTuesday datasets and provide small utilities.
"""

from .guten import list_aliases, load_all

__all__ = ["list_aliases", "load_all"]
