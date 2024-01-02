import openpyxl
import pytest
import requests

from src.constants.api_constants import url_create_token
from src.helpers.api_requests_wrapper import post_request
from src.helpers.utils import common_headers_json


def read_credentials_from_excel(filepath):
    credentials = []
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username":username,
        "password":password
    }
    response = post_request(url=url_create_token(), auth=None, headers=common_headers_json(),
                            payload= payload ,in_json=False)
    return response


def test_post_create_token():
    filepath = "tests/datadriventesting/testdata_ddt.xlsx"
    credentials = read_credentials_from_excel(filepath)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = make_request_auth(username, password)
        print(response)

