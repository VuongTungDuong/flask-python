from peewee import Model
from modules.database.setup import db


class BaseModel(Model):
  class Meta:
    database = db
