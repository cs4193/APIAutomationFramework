from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import url_create_booking
import pytest

from src.helpers.common_verification import verify_json_key_for_not_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json


class TestCreateBooking(object):
    def test_create_booking_tc1(self):
        #URL, Headers, Payload
        response = post_request(url=url_create_booking(),auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_json_key_for_not_none(response.json()["bookingid"])
        verify_http_status_code(response,200)

    def test_create_booking_tc2(self):
        #URL, Headers, Payload
        response = post_request(url=url_create_booking(),auth=None, headers=common_headers_json(),
                                payload={}, in_json=False)

        verify_http_status_code(response,500)

    def test_create_booking_tc3(self):
        # URL, Headers, Payload
        response = post_request(url=url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=None, in_json=False)

        verify_http_status_code(response, 400)
