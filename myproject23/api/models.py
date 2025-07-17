from django.db import models
from django.db import models

class NewStudent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    passby = models.CharField(max_length=50)

    def __str__(self):
        return self.name