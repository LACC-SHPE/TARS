from flask import Flask
from flask_cors import CORS
from logger import TarsLogger

app = Flask(__name__)
CORS(app)

logging = TarsLogger()
