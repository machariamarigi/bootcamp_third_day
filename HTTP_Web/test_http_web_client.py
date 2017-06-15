import unittest

from http_web_client import http_web_client, request_user


class HttpWebClient(unittest.TestCase):
    """Class to test if the http web client module"""

    def test_request_url(self):
        """Test if connection to api is working"""
        response = http_web_client('machariamarigi')
        self.assertIsNotNone(response)


class GetUserTest(unittest.TestCase):
    """Class to test the get_user method"""

    def test_if_input_is_string(self):
        with self.assertRaises(ValueError):
            request_user()


if __name__ == '__main__':
    unittest.main()
