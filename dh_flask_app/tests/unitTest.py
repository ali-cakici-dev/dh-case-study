import unittest
import requests
import json


class TestFlask(unittest.TestCase):
    baseUrl = "http://127.0.0.1:5000"
    testUrl = "http://www.google.codm"
    shortUrl = "253d14"

    def test_server_online(self):
        url = self.baseUrl + "/isOnline"
        headers = {'Cache-Control': "no-cache"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertEqual(r["status"], "success", "Flask server offline")

    def test_url(self):
        url = self.baseUrl + "/addUrl"
        payload = {"url": self.testUrl}
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        self.shortUrl = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10).text
        self.assertGreaterEqual(len(self.shortUrl), 0, "Flask server can not add url ")

    def test_get_all_url(self):
        url = self.baseUrl + "/getAll"
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertGreaterEqual(len(r["urls"]), 0, "Flask server can not get all urls ")

if __name__ == '__main__':
    unittest.main()
