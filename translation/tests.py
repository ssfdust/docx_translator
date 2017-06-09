from django.test import TestCase
from django.test import client

# Create your tests here.
class ResponseTest(TestCase):

    """Docstring for ResponseTest. """

    def __init__(self):
        """TODO: to be defined1. """
        TestCase.__init__(self)

        c = client()
