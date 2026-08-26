"""Llama Librarian application package.

This module intentionally keeps imports light so that submodules such as
``app.main`` can be imported without triggering circular dependencies.
"""

from typing import Any

__all__ = ["__version__", "create_app"]

__version__ = "0.1.0"


def create_app() -> Any:
    """Create and return the configured FastAPI application.

    The import is deferred so that importing the ``app`` package alone does
    not require FastAPI or the rest of the application to be importable.
    """
    from app.main import create_app as _create_app

    return _create_app()