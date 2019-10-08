from django.db import models

# Create your models here.

class Location(models.Model):
    place = models.CharField(max_length =12)
    

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length =15)

    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.CharField(max_length =30)
    location = models.ForeignKey(Location)
    Category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    

    def __str__(self):
        return self.description

    @classmethod
    def search_by_Category(cls,search_term):
        images = cls.objects.filter(Category__name__icontains=search_term)
        return images

