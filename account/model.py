from peewee import CharField, IntegerField
from peewee import Model


class Account(Model):
  registerID = IntegerField(primary_key=True)
  login = CharField(20, null=False)
  password = CharField(40, null=False)
  phone = CharField(20, null=False)
