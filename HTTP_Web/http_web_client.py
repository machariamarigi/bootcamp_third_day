from urllib.request import urlopen, Request, URLError
import json


def http_web_client(url):
    """
        Client that consumes a public web API
    """

    request = Request(url)

    try:
        response = urlopen(request)
        result = json.loads(response.read().decode('utf-8'))

    except URLError as error:
        return {"Error": str(error)}

    else:
        return result['city']['country']
