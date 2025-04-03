import unittest  # Import Python's built-in testing framework
from app.main import app  # Import the Flask app

class TestApp(unittest.TestCase):  # Define a test class that inherits from unittest.TestCase
    def setUp(self):  # Setup method runs before each test
        self.client = app.test_client()  # Creates a test client for the Flask app

    def test_home(self):  # A test case for the home route
        response = self.client.get("/")  # Sends a GET request to "/"
        self.assertEqual(response.data.decode(), "Hello, Buddy!")  # Check if the response is "Hello, Buddy!"

if __name__ == "__main__":
    unittest.main()  # Run the test when the script is executed
