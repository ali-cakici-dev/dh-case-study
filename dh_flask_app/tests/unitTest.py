import unittest
import requests
import json


class TestFlask(unittest.TestCase):
    baseUrl = "http://127.0.0.1:5000"
    testUrl = "www.test.co2nm"
    shortUrl = "13e81dd6"

    def test_server_online(self):
        url = self.baseUrl + "/is_online"
        headers = {'Cache-Control': "no-cache"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertEqual(r["status"], "success", "Flask server offline")

    def test_url(self):
        url = self.baseUrl + "/addURl"
        payload = {"url": self.testUrl}
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10).json()
        self.shortUrl = r["shortUrl"]
        self.assertEqual(r["status"], "success", "Flask server can not add url ")

        url = self.baseUrl + "/" + r["shortUrl"]
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertEqual(r["url"], self.testUrl, "Flask server can not get url ")

    def test_get_url(self):
        url = self.baseUrl + "/" + self.shortUrl
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertEqual(r["url"], self.testUrl, "Flask server can not get url ")

    def test_get_all_url(self):
        url = self.baseUrl + "/getAll"
        headers = {'Cache-Control': "no-cache", "content-type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10).json()
        self.assertGreaterEqual(len(r["urls"]), 0, "Flask server can not get all urls ")

if __name__ == '__main__':
    unittest.main()
