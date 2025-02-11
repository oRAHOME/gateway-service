from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app=app)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()