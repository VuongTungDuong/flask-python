import logging
from datetime import datetime
from pathlib import Path
from time import time

from modules.env import env

LOG_PATH = Path(__file__).parent.parent.joinpath("logs", "errors.log").absolute()


class LoggingFormatter(logging.Formatter):
  GREY = "\x1b[38;20m"
  YELLOW = "\x1b[33;20m"
  RED = "\x1b[31;20m"
  BOLD_RED = "\x1b[31;1m"
  RESET = "\x1b[0m"
  FORMAT = "%(asctime)s - [%(process)d] - [%(name)s:%(lineno)d] - %(message)s"
  FORMATS = {
    logging.DEBUG: YELLOW + FORMAT + RESET,
    logging.INFO: GREY + FORMAT + RESET,
    logging.WARNING: YELLOW + FORMAT + RESET,
    logging.ERROR: RED + FORMAT + RESET,
    logging.CRITICAL: BOLD_RED + FORMAT + RESET,
  }

  def format(self, record):
    log_fmt = self.FORMATS.get(record.levelno)
    formatter = logging.Formatter(log_fmt)
    return formatter.format(record)


def use_logger(name: str, level=logging.DEBUG):
  logger = logging.getLogger(name)

  if not env.DEBUG:
    if not LOG_PATH.parent.exists():
      LOG_PATH.parent.mkdir()

    today = datetime.today().strftime("%Y_%m_%d")
    path = LOG_PATH.with_suffix(LOG_PATH.suffix + "." + today)
    handler = logging.FileHandler(path, delay=True)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
      "%(asctime)s - [%(levelname)s] - [%(process)d] - [%(name)s:%(lineno)d] - %(message)s"
    )
    handler.setFormatter(formatter)
  else:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(LoggingFormatter())

  logger.addHandler(handler)
  logger.setLevel(level if env.DEBUG else logging.INFO)

  return logger


def use_file_logger(name: str, path: Path | str, level=logging.INFO):
  path = Path(path).absolute() if isinstance(path, str) else path.absolute()

  path.parent.exists() or path.parent.mkdir(parents=True, exist_ok=True)

  logger = logging.getLogger(name)
  today = datetime.today().strftime("%Y_%m_%d")
  path = path.with_suffix(LOG_PATH.suffix + "." + today)
  handler = logging.FileHandler(path, delay=True)
  formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")

  handler.setFormatter(formatter)
  handler.setLevel(level)

  logger.addHandler(handler)
  logger.setLevel(level)

  return logger


def remove_old_logs(days: int, log_dir: Path | str):
  now = time()
  threshold = now - (days * 86400)

  for file_path in Path(log_dir).iterdir():
    if file_path.is_file() and ".log" in file_path.name:
      file_mod_time = file_path.stat().st_mtime

      if file_mod_time < threshold:
        file_path.unlink()
