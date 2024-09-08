# """
# Copyright (c) 2024 SHPE LACC
# Coded by Dichill and Paola

# This module contains unit tests for the TARS API endpoints.
# It uses the requests library to make HTTP requests to the API
# and unittest for test assertions.
# """

# import unittest
# import requests


# class TestTarsAPI(unittest.TestCase):
#     """
#     A test suite for the TARS API endpoints.
#     """

#     def setUp(self):
#         """
#         Set up the test environment before each test method runs.
#         """
#         self.base_url = (
#             "http://localhost:8080"  # Adjust if your API is hosted elsewhere
#         )

#     def test_move_endpoint(self):
#         """
#         Test the /api/move endpoint.

#         Sends a POST request with a 'left' move command and
#         verifies the response status and content.
#         """
#         response = requests.post(f"{self.base_url}/api/move", json={"move": "left"})
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Moving"})

#     def test_speak_endpoint(self):
#         """
#         Test the /api/speak endpoint.

#         Sends a POST request to the speak endpoint and
#         verifies the response status and content.
#         """
#         response = requests.post(
#             f"{self.base_url}/api/speak", json={"message": "Hello"}
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Speaking"})


import requests


def test_streaming_response():
    url = "http://127.0.0.1:8080/api/ask"
    payload = {"question": "Who leads the SHPE from LACC?"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, stream=True)

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    # Read the streamed response
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            text = chunk.decode("utf-8")
            print(text, end="")


test_streaming_response()
