"""
Copyright (c) 2024 SHPE LACC
Coded by Dichill and Paola

This module defines the Flask API for controlling a robot. It includes endpoints for movement,
speech, and querying the robot's capabilities.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from logger import TarsLogger
from core.GPTAgent import GPTAgent

app = Flask(__name__)
CORS(app)

logging = TarsLogger()
gpt_agent = GPTAgent(logging)


@app.route("/api/move", methods=["POST"])
def move():
    """
    Move the robot based on the command received in the request.

    Expects a JSON payload with a 'move' key. Valid commands are 'left', 'right', 
    'forward', and 'backward'. Returns a confirmation message.

    Returns:
        str: Confirmation message indicating the movement command.
    """
    j = request.get_json()
    mv = j.get("move")
    logging.debug(f"Received query: {mv}")

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
        logging.warning("Invalid movement command received.")
        return jsonify({"error": "Invalid movement command"}), 400

    return jsonify({"message": "Moving"}), 200


@app.route("/api/speak", methods=["POST"])
def speak():
    """
    Speak a message received from the request.

    Expects a JSON payload with a 'message' key. Returns a confirmation message.

    Returns:
        str: Confirmation message indicating the speaking action.
    """
    j = request.get_json()
    message = j.get("message")
    logging.debug(f"Received message to speak: {message}")
    # Implement text-to-speech functionality here
    return jsonify({"message": "Speaking"}), 200


@app.route("/api/ask", methods=["POST"])
def ask():
    """
    Process a question received from the request.

    Expects a JSON payload with a 'question' key. Returns a confirmation message.

    Returns:
        str: Confirmation message indicating the question processing.
    """
    j = request.get_json()
    question = j.get("question")
    logging.debug(f"Received question: {question}")
    # Implement question processing logic here
    return jsonify({"message": "Asking"}), 200


if __name__ == "__main__":
    """
    Start the Flask server.
    """
    logging.info("Server has started")
    app.run("0.0.0.0", port=8080)
