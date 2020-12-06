from django.db import models

STATUS_CHOICES = (
    (0, 'INACTIVE'),
    (1, 'ACTIVE')
)

class Registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name

