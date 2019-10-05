from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length =12)


    def __str__(self):
        return self.location

class Category(models.Model):
     name = models.CharField(max_length =15)

     def __str__(self):
         return self.name


class Image(models.Model):
    description = models.CharField(max_length =30)
    location = models.ForeignKey(Location)
    Category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.description

