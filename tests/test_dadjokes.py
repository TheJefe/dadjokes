import unittest
from django.test import Client

import dadjokes.views

class DadJokesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_dadjokes(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_dadjokes_returns_text(self):
        jokes = ["I'm hilarious"]
        dadjokes.views.JOKES = jokes

        response = self.client.get('/')

        self.assertEqual(response.content.decode(), jokes[0])

