from django.test import TestCase, Client
from django.contrib.auth import get_user_model

class TestSome(TestCase):

  def setUp(self):
    self.client = Client()
    
  def test_get(self):
    response = self.client.login(username='admin', password='admin')

  def test_create_superuser(self):
    """ Creación de superusuario correcta """
    username = 'test@test.com'
    password = 'test123'
    superuser = get_user_model().objects.create_superuser(
      username = username,
      password = password
    )

    self.assertTrue(superuser.is_staff)

  def test_create_user_with_email_successful(self):
    """ Probar, crear un nuevo usuario con un email correctamente """
    
    username = 'test@datadosis.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(
      username=username,
      password=password
    )
    
    self.assertEqual(user.username, username)
    self.assertTrue(user.check_password(password))

  def test_new_user_invalid_email(self):
    """ Nuevo usuario email invalido """
    
    with self.assertRaises(ValueError):
      user = get_user_model().objects.create_user(username=None, password='Testpass123')
  
  def test_get_method(self):
    """ Comprobar la correcta visualización de get """
    response = self.client.get('/api/tasks/')
    
    self.assertEqual(response.status_code, 200)

  def test_post_method(self):
    """ Comprobar el correcto envio de información """
    request = self.client.post('/api/tasks/', {
      "username": "test",
      "name_task": "test",
      "description": "test",
      "attached_file": ""
    })
    self.assertEqual(request.status_code, 201)

  def test_put_method(self):
    """ Comprobar la acualización de la información """
    action = self.client.put('/api/tasks/1/', {
    "id": 1,
    "username": "krespo",
    "name_task": "Clinica Colombia",
    "description": "Reunión para definir los requerimientos de la fase numero 3 de desarrollo",
    "attached_file": ""
    })
    self.assertEqual(action.status_code, 404)

  def test_delete_method(self):
    """ Comprobar la eliminacion de la informacion """
    delete = self.client.delete('/api/tasks/1/')
    self.assertEqual(delete.status_code, 404)