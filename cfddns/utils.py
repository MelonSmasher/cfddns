from requests import get


def get_external_ip(urls):
    """
    :return:
    """
    for url in urls:
        response = get(url)
        if response.ok:
            return response.text
    return False
