from flask import Flask, request
from flask_cors import CORS
from logger import TarsLogger
from core.GPTAgent import GPTAgent

# Prompt Engineering for ChatGPT
# Chat GPT -> Paola
# Voice Recognition -> Deshell
# Text to Speech (?) -> Deshell

app = Flask(__name__)
CORS(app)

logging = TarsLogger()
gpt_agent = GPTAgent(logging)


@app.route("/api/move", methods=["POST"])
def move():
    # get the movement from the request
    # move the robot
    # get query from the request
    j = request.get_json()
    mv = j["move"]
    logging.info(f"Received query: {mv}")
    if mv == "left":
        # move left
        pass
    elif mv == "right":
        # move right
        pass
    elif mv == "forward":
        # move forward
        pass
    elif mv == "backward":
        # move backward
        pass
    else:
        # handle invalid query
        pass

    return "Moving"


@app.route("/api/speak", methods=["POST"])
def speak():
    # get the message from the request and speak it (text-to-speech module), request is from
    # GPT's response
    return "Speaking"


@app.route("/api/ask", methods=["POST"])
def ask():
    # get the question from the request
    j = request.get_json()
    question = j["question"]
    logging.info(f"Received question: {question}")


if __name__ == "__main__":
    # start the server
    app.run("0.0.0.0", port=8080)
