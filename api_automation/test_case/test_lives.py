#!/usr/bin/env python3

import unittest


class TestLives(unittest.TestCase):
    url = "https://api.520yidui.com/v2/lives"
    headers = get_headers_by_test_account("18310061886", "1886")
    params = {"page": 1}

    @classmethod
    def setUpClass(cls):
        logger().info("test lives begin!")

    @classmethod
    def tearDownClass(cls):
        logger().info("test lives finished!")

    def test_response_body(self):
        lives = Lives(self.url, headers=self.headers, parmas=self.params)
        self.assertNotEqual(lives.get_response_body(), 0)


if __name__ == '__main__':
    unittest.main()
