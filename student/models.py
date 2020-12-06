from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=500)

