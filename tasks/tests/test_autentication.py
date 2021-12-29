# Django
from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class TestAutentication(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.client.login(username='test', password='secretpass')

  def test_token(self):
    token = Token.objects.get(user__username='test')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
