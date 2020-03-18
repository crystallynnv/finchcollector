from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model): 
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})

# finches = [
#   Finch('Lolo', 'tabby', 'foul little demon', 3),
#   Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Finch('Raven', 'black tripod', '3 legged cat', 4)
# ]