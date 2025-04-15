from modules.database.setup import db
from account.model import Account


db.create_tables([Account])
