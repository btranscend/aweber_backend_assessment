from django.db import models

# Create your models here.
class Widgets(models.Model):
    name = models.CharField(max_length=64)
    number_of_parts = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
