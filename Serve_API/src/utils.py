from typing import List, Dict
import json
import logging
import requests


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def do_prediction(url:str, data:Dict[str,List]) -> requests.models.Response:
    if data:
        data_json = json.dumps(data)
        headers = {"content-type": "application/json"}
        try:
            response = requests.post(url, data=data_json, headers=headers, timeout = 3)

        except requests.exceptions.Timeout:
            return None

        else:
            if response.ok:
                return response
            else:
                logging.error(f'Trouble getting a response for the API')
                return None

