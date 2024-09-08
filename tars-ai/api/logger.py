"""
Copyright (c) 2024 SHPE LACC
Coded by Dichill and Paola

This module defines a custom logger for the TARS AI project.
"""

import logging


class TarsLogger:
    """
    A custom logger class for the TARS AI project.

    This class sets up logging with both console and file handlers,
    allowing for flexible logging across the application.
    """

    def __init__(self):
        """
        Initialize the TarsLogger.

        Sets up the logger with console and file handlers, and configures
        the logging format.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        self.console_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler(
            "./logs/app.log", mode="a", encoding="utf-8"
        )

        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)

        self.formatter = logging.Formatter(
            "{asctime} - {levelname} - {message}",
            style="{",
            datefmt="%Y-%m-%d %H:%M",
        )

        self.console_handler.setFormatter(self.formatter)
        self.file_handler.setFormatter(self.formatter)

        self.logger.info("Logger is now initialized")

    def info(self, message):
        """
        Log an info message.

        Args:
            message (str): The message to be logged.
        """
        self.logger.info(message)

    def debug(self, message):
        """
        Log a debug message.

        Args:
            message (str): The message to be logged.
        """
        self.logger.debug(message)

    def error(self, message):
        """
        Log an error message.

        Args:
            message (str): The message to be logged.
        """
        self.logger.error(message)

    def warning(self, message):
        """
        Log a warning message.

        Args:
            message (str): The message to be logged.
        """
        self.logger.warning(message)
