from src.helpers.api_requests_wrapper import post_request, patch_request, delete_request
from src.constants.api_constants import url_create_booking, url_create_token, url_patch_put_delete_booking
import pytest

from src.helpers.common_verification import verify_json_key_for_not_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token, payload_update_booking
from src.helpers.utils import common_headers_json, patch_headers_json


class TestCRUDOperations(object):

    def test_update_booking(self,create_token,create_booking):

        token2 = create_token
        booking_id = create_booking

        response = patch_request(url=url_patch_put_delete_booking(booking_id),auth=None,headers=patch_headers_json(token2),
                                payload=payload_update_booking(), in_json=False)
        print(response.status_code)
        print(response.json())

    def test_delete_booking(self,create_token,create_booking):
        token2 = create_token
        booking_id = create_booking
        response = delete_request(url = url_patch_put_delete_booking(booking_id),auth= None,
                                  headers=patch_headers_json(token2),
                                  in_json=False)
        print(response)

