from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester("https://www.google.com/")

    def test_make_request(self):
        with patch("requests.get") as mocked_get:
            response = self.page.get()
            print(response.rolf)
            mocked_get.assert_called()

    def test_content_returned(self):
        fake_content = "Hello"

        class FakeResponse:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()):
            result = self.page.get()
            self.assertEqual(result, fake_content)
