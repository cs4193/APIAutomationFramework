import json
import os
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import url_create_booking
import pytest

from src.helpers.common_verification import verify_json_key_for_not_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_booking_dynamic
from src.helpers.utils import common_headers_json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

class TestCreateBooking(object):

    def load_schema(self,schema_file):
        with open(schema_file,'r') as file:
            return json.load(file)


    def test_create_booking_tc1(self):
        #URL, Headers, Payload
        response = post_request(url=url_create_booking(),auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_json_key_for_not_none(response.json()["bookingid"])
        verify_http_status_code(response,200)
        response_json = response.json()
        file_path = os.getcwd() + "/schema.json"
        schema = self.load_schema(file_path)

        try:
            validate(instance=response_json,schema=schema)
        except ValidationError as e:
            print(e.message)

    def test_create_booking_tc4(self):
        # URL, Headers, Payload
        response = post_request(url=url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking_dynamic(), in_json=False)

        verify_http_status_code(response, 200)


