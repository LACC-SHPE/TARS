from flask import Flask
from flask_cors import CORS
from logger import TarsLogger
import settings

app = Flask(__name__)
CORS(app)

logging = TarsLogger()

logging.info("Hello Paola")
# Chat GPT
# Voice Recognition
# Text to Speech (?)


# if __name__ == "__main__":
#     app.run()
