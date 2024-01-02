#common Headers

def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers


def patch_headers_json(token2):
    token1 = "token="+token2
    headers = {
        "Content-Type": "application/json",
        "Cookie": token1
    }
    return headers
