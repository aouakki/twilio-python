import unittest
from tests.integration.holodeck import Holodeck
from twilio.http.response import Response
from twilio.rest import Twilio


class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.account_sid = 'AC' + 'a' * 32
        self.auth_token = 'AUTHTOKEN'
        self.holodeck = Holodeck()
        self.twilio = Twilio(account_sid=self.account_sid,
                             auth_token=self.auth_token,
                             http_client=self.holodeck)