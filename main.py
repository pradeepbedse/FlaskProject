from flask import Flask, render_template, request, redirect, url_for
from flask.wrappers import Response

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello World'


if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)
