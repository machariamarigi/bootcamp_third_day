import unittest

from http_web_client import http_web_client


class HttpWebClient(unittest.TestCase):
    """Class to test if the http web client module"""

    def test_it_works(self):
        result = http_web_client(
            'http://api.openweathermap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff')
        self.assertEqual(result, 'KE', "Not working")

    def test_bad_url(self):
        result = http_web_client(
            'http://api.odsrmap.org/data/2.5/forecast/daily?q=Nairobi&APPID=9e68c31e59d752247d58d439c50aaaff')
        self.assertDictEqual(
            result,
            {'Error': '<urlopen error [Errno -2] Name or service not known>'},
            "Not working")

if __name__ == '__main__':
    unittest.main()
