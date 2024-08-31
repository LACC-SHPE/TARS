import logging


class TarsLogger:
    def __init__(self):
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

        self.logger.info("Logger initialized")

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)
