from django.db import models

# Create your models here.
class Tasks(models.Model):
  username = models.CharField(max_length=100, blank=False)
  name_task = models.CharField(max_length=100, blank=False)
  description = models.CharField(max_length=100, blank=False)
  attached_file = models.FileField(blank=True, null=True)

  def __str__(self):
    return self.username