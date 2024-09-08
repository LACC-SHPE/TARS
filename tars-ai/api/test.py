"""
Copyright (c) 2024 SHPE LACC
Coded by Dichill and Paola

This module contains unit tests for the TARS API endpoints.
It uses the requests library to make HTTP requests to the API
and unittest for test assertions.
"""

import unittest
import requests


class TestTarsAPI(unittest.TestCase):
    """
    A test suite for the TARS API endpoints.
    """

    def setUp(self):
        """
        Set up the test environment before each test method runs.
        """
        self.base_url = (
            "http://localhost:8080"  # Adjust if your API is hosted elsewhere
        )

    def test_move_endpoint(self):
        """
        Test the /api/move endpoint.

        Sends a POST request with a 'left' move command and
        verifies the response status and content.
        """
        response = requests.post(f"{self.base_url}/api/move", json={"move": "left"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Moving"})

    def test_speak_endpoint(self):
        """
        Test the /api/speak endpoint.

        Sends a POST request to the speak endpoint and
        verifies the response status and content.
        """
        response = requests.post(
            f"{self.base_url}/api/speak", json={"message": "Hello"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Speaking"})

    def test_ask_endpoint(self):
        """
        Test the /api/ask endpoint.

        This test method sends a POST request to the /api/ask endpoint
        with a sample question and verifies the response.

        The test checks for:
        1. The correct status code (200 OK)
        2. The response content type (text/event-stream)
        3. The presence of a non-empty response

        Note: This test does not validate the specific content of the response,
        as it may vary depending on the AI model's output.
        """
        question = "Who is fahat and dichill?"
        response = requests.post(
            f"{self.base_url}/api/ask", json={"question": question}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "text/event-stream")

        # Check if the response content is not empty
        self.assertTrue(len(response.content) > 0)


if __name__ == "__main__":
    unittest.main()
