from src.constants.api_constants import Base_url, base_url, APIConstants


def test_crud():
    print(Base_url)

    url = base_url()
    print(url)

    url1 = APIConstants.url_patch_put_delete_booking(self=object, booking_id=121)
    print(url1)

    url2 = APIConstants.base_url()
    print(url2)