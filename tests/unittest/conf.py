import unittest

from app import create_app
from dotenv import load_dotenv

""" Basic Config to run the test """


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        load_dotenv()
        cls.app = create_app(test=True)

    def setUp(self):
        super(BaseTestCase, self).setUp()
        load_dotenv(())
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
