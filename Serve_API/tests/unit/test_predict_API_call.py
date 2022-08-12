import unittest
from unittest.mock import patch, MagicMock

from Serve_API.src.Models import CarModel
from Serve_API.src.predict_API_call import PredictAPI


__author__ = 'Anand Devarajan'

class TestApiCall(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.API_call = PredictAPI()


    @patch('Serve_API.src.predict_API_call.do_prediction')
    def test_success_single_input(self, mock_do_prediction):
        """ It tests the Successful execution of the predict_single_input method"""
        dummy_json = {'predictions': [[15.8185673]]}
        mock_value = MagicMock()
        mock_value.return_value = dummy_json
        mock_do_prediction.return_value = mock_value

        si = self.API_call.predict_single_input(8, 390.0, 190, 3850.0, 8.5, 70, 0, 0, 1)
        self.assertEqual(si.return_value,dummy_json)

    @patch('Serve_API.src.predict_API_call.do_prediction')
    def test_success_multiple_input(self, mock_do_prediction):
        """ It tests the Successful execution of the test_success_multiple_input method"""
        dummy_json = {'predictions': [[15.8185673], [15.8185673]]}
        car = CarModel(Cylinders=8,Displacement=390.0,Horsepower=190,
                       Weight=3850.0,Acceleration=8.5,Model_Year=70,
                       Europe=0,Japan=0,USA=1)

        mock_value = MagicMock()
        mock_value.return_value = dummy_json
        mock_do_prediction.return_value = mock_value

        mi = self.API_call.predict_multiple_input([car,car])
        self.assertEqual(mi.return_value, dummy_json)


if __name__ == '__main__':
    unittest.main()
