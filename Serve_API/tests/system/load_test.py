import json
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser

__author__ = 'Anand Devarajan'

log = logging.getLogger("rest-api-load-test")

def get_headers():
    """ It generated the api headers."""
    headers = {
        "Content-Type": "application/json"
    }
    return headers

def get_api_payload():
    """ It generated the body of request."""
    payload = {
    }
    return payload


class LocustClient(FastHttpUser):
    host = "http://127.0.0.1:8000/predict/"
    wait_time = constant(0)

    def __init__(self,environment):
        super().__init__(environment)

    def on_start(self):
        pass
    def on_stop(self):
        pass

    @task
    def load_rest_api_based_service(self):
        try:

            headers = get_headers()
            api_query_params = '?Cylinders=8&Displacement=390.0&Horsepower=190&Weight=3850.0&Acceleration=8.5&Model_Year=70&Europe=0&Japan=0&USA=1'
            api_payload = json.dumps(get_api_payload())

            with self.client.get(api_query_params, headers = headers,
                                 catch_response=True, data=api_payload,
                                 name="Predict dnn model"
                                 ) as resp_of_api:

                if resp_of_api.status_code == 200:
                    resp_body_of_api = resp_of_api.json()
                    assert resp_body_of_api == {'predictions': [[15.8185673]]}

                    resp_of_api.success()

                    log.info("API call resulted in success.")

                else:
                    resp_of_api.failure(resp_of_api.text)

                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")