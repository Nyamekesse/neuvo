import os

# logging.basicConfig(
#     filename="logs/exceptions.log",
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s: %(message)s",
# )

# logger = logging.getLogger("app")


LOGS_DIR = os.path.abspath("logs")
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s %(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "requests": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "level": "DEBUG",
            "filename": os.path.join(LOGS_DIR, "requests.log"),
            "when": "midnight",
            "backupCount": 30,
        },
        "exceptions": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "level": "ERROR",
            "filename": os.path.join(LOGS_DIR, "exceptions.log"),
            "when": "midnight",
            "backupCount": 30,
        },
    },
    "loggers": {
        "werkzeug": {
            "handlers": ["console", "requests"],
            "level": "DEBUG",
            "propagate": False,
        },
        "app": {
            "handlers": ["console", "exceptions"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
