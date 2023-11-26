from django.db import models


class Table_1(models.Model):
    name = models.CharField(max_length=20)
    unit = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
