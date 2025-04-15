from dataclasses import dataclass
from pathlib import Path

from dotenv import dotenv_values


@dataclass
class Env:
  DEBUG: bool
  SERVER_PORT: int

  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  DATABASE_NAME: str


print(__file__)

env = Env(**dotenv_values(Path(__file__).absolute().parent.joinpath("../.env")))
