import os
from flask import Flask, session

from blueprints.blue import blueprint

app = Flask(__name__)

# Todas las rutas de nuestro blueprint serana accesadas desde /blue/url
app.register_blueprint(blueprint, url_prefix='/blue')

@app.route('/')
def index():
  return "Hello nice"

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=int("80"),debug=True)
	