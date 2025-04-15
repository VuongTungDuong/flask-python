from bootstrap.type import OpenSwagger
from flask import Flask, render_template, request
from flask_smorest import Api
from bootstrap.route import api_v1

app = Flask(__name__)

swagger: OpenSwagger = {
  "API_TITLE": "API Docs",
  "API_VERSION": "v1",
  "OPENAPI_VERSION": "3.0.3",
  "PROPAGETE_EXCEPTIONS": True,
  "OPENAPI_URL_PREFIX": "/",
  "OPENAPI_SWAGGER_UI_PATH": "/docs",
  "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
}

app.config.update(swagger)

api = Api(app)

api.register_blueprint(api_v1)


@app.route("/")
def home():
  print(request)
  return render_template("home.html")
