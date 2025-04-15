from bootstrap.app import app
from modules.env import env

if "__main__" == __name__:
  app.run("0.0.0.0", port=env.SERVER_PORT, debug=env.DEBUG)
