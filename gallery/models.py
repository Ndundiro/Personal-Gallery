from django.db import models

# Create your models here.
class Image(models.Model):
    description = models.CharField(max_length =30)

    def __str__(self):
        return self.description
