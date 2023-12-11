from src.helpers.api_requests_wrapper import post_request, patch_request, delete_request
from src.constants.api_constants import url_create_booking, url_create_token, url_patch_put_delete_booking
import pytest

from src.helpers.common_verification import verify_json_key_for_not_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers_json, patch_headers_json


class TestCRUDOperations(object):
    def test_create_token(self):
        response = post_request(url=url_create_token(), auth=None, headers=common_headers_json(),
                                payload=payload_create_token(),in_json=False)
        print(response)
        token1 = response.json()["token"]
        print(token1)
        verify_http_status_code(response, 200)

    def test_create_booking_tc1(self):
        #URL, Headers, Payload
        response = post_request(url=url_create_booking(),auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_json_key_for_not_none(response.json()["bookingid"])
        verify_http_status_code(response,200)

    def test_update_booking(self):

        token2 = "0823593f4a62400"
        booking_id = 3127
        auth = ("admin","password123")
        response = patch_request(url=url_patch_put_delete_booking(3414),auth=None,headers=patch_headers_json(),
                                payload=payload_update_booking(), in_json=False)
        print(response.status_code)
        print(response.json())

    def test_delete_booking(self):
        response = delete_request(url = url_patch_put_delete_booking(3414),auth= None, headers=patch_headers_json(),
                                  in_json=False)
        print(response)

