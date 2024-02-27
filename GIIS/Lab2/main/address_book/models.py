from django.db import models


# Create your models here.
class ContactModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}. {self.last_name} {self.first_name} {self.surname}"
