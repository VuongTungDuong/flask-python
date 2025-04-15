from peewee import PostgresqlDatabase
from modules.env import env

connect_db = PostgresqlDatabase(
  database=env.DATABASE_NAME,
  host="db",
  user=env.POSTGRES_USER,
  password=env.POSTGRES_PASSWORD,
)

connect_db.connect()

connect_db.close()
