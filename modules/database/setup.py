from peewee import PostgresqlDatabase
from modules.env import env

db = PostgresqlDatabase(
  database=env.DATABASE_NAME,
  host="db",
  user=env.POSTGRES_USER,
  password=env.POSTGRES_PASSWORD,
)
