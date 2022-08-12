import unittest
from seleniumwire import webdriver
import chromedriver_autoinstaller
import json

__author__ = 'Anand Devarajan'
class TestSignup(unittest.TestCase):

    def setUp(self):
        chromedriver_autoinstaller.install()

        self.driver = webdriver.Chrome()
        self.url = 'http://127.0.0.1:8000/predict/?Cylinders=8&Displacement=390.0&Horsepower=190&Weight=3850.0&Acceleration=8.5&Model_Year=70&Europe=0&Japan=0&USA=1'


    def test_get_response(self):
        """It the test the whole api as an entity"""
        # Go to predict url
        self.driver.get(self.url)

        # Access requests via the `requests` attribute
        response = self.driver.requests[0].response
        response_body = response.body.decode('utf-8')
        response_body_json = json.loads(response_body)

        self.assertIn("http://127.0.0.1:8000/predict/", self.driver.current_url)
        self.assertEqual(200, response.status_code)
        self.assertEqual([[15.8185673]], response_body_json['predictions'])

    def tearDown(self):
        self.driver.quit


if __name__ == '__main__':
    unittest.main()

