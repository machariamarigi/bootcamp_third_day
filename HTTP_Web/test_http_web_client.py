import unittest

from http_web_client import http_web_client, request_user


class HttpWebClient(unittest.TestCase):
    """Class to test if the http web client module"""

    def test_request_url(self):
        """Test if connection to api is working"""
        response = http_web_client('machariamarigi')
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
