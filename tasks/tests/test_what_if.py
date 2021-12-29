from types import SimpleNamespace
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

class TestWhatIfModels(TestCase):

  def setUp(self):
    self.client = Client()

  def test_post_method_fail_one(self):
    """ Comprobar el correcto funcionamiento si llega a intentar enviarse un elemento vacio diferente a attached_file """
    request = self.client.post('/api/tasks/', {
      "username": "",
      "name_task": "test",
      "description": "test",
      "attached_file": ""
    })
    self.assertEqual(request.status_code, 400)

  def test_post_method_fail_two(self):
    """ Comprobar el correcto funcionamiento si llega a intentar enviarse un elemento vacio diferente a attached_file """
    request = self.client.post('/api/tasks/', {
      "username": "test",
      "name_task": "",
      "description": "test",
      "attached_file": ""
    })
    self.assertEqual(request.status_code, 400)

  def test_post_method_fail_three(self):
    """ Comprobar el correcto funcionamiento si llega a intentar enviarse un elemento vacio diferente a attached_file """
    request = self.client.post('/api/tasks/', {
      "username": "test",
      "name_task": "test",
      "description": "",
      "attached_file": ""
    })
    self.assertEqual(request.status_code, 400)

  def test_file(self):
    """ Envio del archivo file exitoso """
    with open('tasks/tests/resources/test.csv', mode="rb") as file:
      file = SimpleUploadedFile(file.name, file.read(), content_type='file/csv')
      response = self.client.post('/api/tasks/',{
          "username": "test",
          "name_task": "test",
          "description": "test",
          "attached_file": file
      })
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)