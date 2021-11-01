import requests


def get_external_ip(urls):
    """
    :return:
    """
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.ConnectionError as e:
            #print(e)
            pass
    return False
