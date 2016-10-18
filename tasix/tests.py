# Django
from django.test import TestCase
from django.http import HttpResponseForbidden

# Mock
from mock import Mock

# Tasix
from tasix.middleware import TasixMiddleware


class TasixMiddlewareTest(TestCase):

    def setUp(self):
        self.middleware = TasixMiddleware()
        self.request = Mock()
        self.request.session = dict()

    def test_with_non_tasix_ip(self):
        self.request.META = dict()
        self.request.META['REMOTE_ADDR'] = '8.8.8.8'
        self.assertEquals(
            403,
            self.middleware.process_request(self.request).status_code)
        self.assertIsInstance(
            self.middleware.process_request(self.request),
            HttpResponseForbidden)

    def test_should_raise_keyerror_exception(self):
        self.request.META = dict()
        with self.assertRaises(KeyError):
            self.assertIsInstance(
                self.middleware.process_request(self.request),
                HttpResponseForbidden)

    def test_should_raise_typeerror_exception(self):
        with self.assertRaises(TypeError):
            self.assertIsInstance(
                self.middleware.process_request(self.request),
                HttpResponseForbidden)
