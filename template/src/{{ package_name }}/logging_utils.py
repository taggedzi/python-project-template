"""Logging helpers."""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logging(level: str = "INFO", log_file: str | None = None) -> None:
    numeric = logging.getLevelName(level.upper())
    if isinstance(numeric, str):
        numeric = logging.INFO

    handlers = None
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers = [logging.FileHandler(log_path, encoding="utf-8")]

    logging.basicConfig(
        level=numeric,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=handlers,
    )
