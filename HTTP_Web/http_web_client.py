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
        Function to prompt user to enter their github username and outputs
        their github fullname, link to their page and bio
    """
    username = raw_input('Please enter a valid github username: ')

    if isinstance(username, str):
        user_profile = http_web_client(username)
        if user_profile == None:
            print('That was not a correct username')
            request_user()
        else:
            github_name = user_profile['name']
            github_link = user_profile['html_url']
            github_bio = user_profile['bio']
            print('User is {}'.format(github_name))
            print('Bio:'.format(github_bio))
            print('Profile page => {}'.format(github_link))
            print('Bye')
    else:
        raise ValueError('Input is not a valid string')

request_user()
