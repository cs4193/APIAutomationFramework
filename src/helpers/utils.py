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


def patch_headers_json():
    headers = {
        "Content-Type": "application/json",
        "Cookie": "token=c351b71011b78f9"
    }
    return headers
