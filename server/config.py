from decouple import config
import os

DB_NAME = config("DB_NAME")
DB_TESTING_NAME = config("DB_TESTING_NAME")
DB_USERNAME = config("DB_USERNAME")
DB_USER_PASS = config("DB_USER_PASS")
DB_CONNECTION_PORT = config("DB_CONNECTION_PORT")


class Config:
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool)


class Logging:
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
                "propagate": True,
            },
            "app": {
                "handlers": ["console", "exceptions"],
                "level": "ERROR",
                "propagate": True,
            },
        },
    }


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_USER_PASS}@{DB_CONNECTION_PORT}/{DB_NAME}"
    )
    DEBUG = config("DEBUG", cast=bool)
    # SQLALCHEMY_ECHO = config("SQLALCHEMY_ECHO", cast=bool)


class ProConfig(Config):
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_USER_PASS}@{DB_CONNECTION_PORT}/{DB_TESTING_NAME}"
    SQLALCHEMY_ECHO = False
    TESTING = True
