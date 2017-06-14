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
        if result['city']['country']:
            return result['city']['country']
        else:
            return result


def request_url():
    """
        Function to prompt user enter an url of a public ApI
    """
    input_url = input('Please enter a public API url: ')
    print(http_web_client(input_url))

request_url()
