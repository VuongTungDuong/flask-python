from model.setup import connect_db


def db(f):
  connect_db.connect()
  try:

    def decorator_fun(*agrs, **kwargs):
      return f(*agrs, **kwargs)

    return decorator_fun

  finally:
    connect_db.close()
