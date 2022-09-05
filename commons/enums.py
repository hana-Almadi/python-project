"""
common enums used in multiple apps
"""

from enum import Enum


class AppName(str, Enum):
    APP1 = "app1"
    APP2 = "app2"

    @classmethod
    def list(cls):
        return {AppName.APP1.value,
                AppName.APP2.value}


class LoggingLevel(str, Enum):
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARN = "WARN"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"
