"""Service layer for Llama Librarian.

This package groups the domain services used by the FastAPI application.

Modules:
- claims: Markdown parsing and claim extraction.
- importer: Patron and claim creation from Markdown notes.
- embeddings: Local-first embedding generation.
- debates: Conflict and overlap detection.
- librarian: Fines, shush levels, shelf relocations, and resolution rules.
"""

from importlib import import_module

__all__ = [
    "claims",
    "debates",
    "embeddings",
    "importer",
    "librarian",
]


def __getattr__(name):
    """Lazily import service submodules when they are accessed."""
    if name in __all__:
        module = import_module(f".{name}", __name__)
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    """Expose service submodules in introspection and tab completion."""
    return sorted(set(__all__) | set(globals().keys()))