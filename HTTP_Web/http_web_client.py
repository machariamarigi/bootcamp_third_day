import requests
import json


def http_web_client(user):
    """
        Client that consumes a public web API
    """

    profile = requests.get('https://api.github.com/users/' + user)

    if profile.ok:
        data = profile.json()
        return data
    else:
        return None


def request_user():
    """
        Function to prompt user to enter their github usernae
    """
    pass

