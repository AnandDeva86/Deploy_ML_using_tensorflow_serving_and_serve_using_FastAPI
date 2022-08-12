import unittest
from unittest.mock import patch, MagicMock
import requests

from Serve_API.src.utils import do_prediction


class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.instance = {"instances": [[8, 390.0, 190, 3850.0, 8.5, 70, 0, 0, 1]]}
        cls.url = "http://localhost:8501/v1/models/saved_model/versions/1:predict"


    @patch('Serve_API.src.utils.requests.post')
    def test_success(self, mock_object):

        mock_value = MagicMock()
        mock_value.status_code = 200
        mock_value.json.return_value = self.instance
        mock_object.return_value = mock_value

        do = do_prediction(self.url,self.instance)
        self.assertEqual(do.status_code, 200)

    @patch('Serve_API.src.utils.requests.post')
    def test_failure(self, mock_object):

        mock_value = MagicMock(status_code = 404)
        mock_value.json.return_value = self.instance
        mock_object.return_value = mock_value

        do = do_prediction(self.url,self.instance)
        self.assertEqual(do.status_code, 404)

    @patch('Serve_API.src.utils.requests.post')
    def test_timeout_exception(self, mock_object):
        mock_object.side_effect = requests.exceptions.Timeout('Server timed out')
        do = do_prediction(self.url, self.instance)
        self.assertEqual(do, None)


if __name__ == '__main__':
    unittest.main()

