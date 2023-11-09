from django.db import models

# Create your models here.





class Teachers(models.Model):
    name = models.CharField(max_length = 100, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    image = models.ImageField(upload_to = "uploads/images", default="uploads/images/profile.jpg")

    def __str__(self):
        return self.name



class Shop(models.Model):
    image = models.ImageField(upload_to="uploads/images")
    item = models.CharField(max_length= 100, blank=False, null=False)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.item

    

class Blog(models.Model):
    image = models.ImageField(upload_to="uploads/images")
    title = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length= 100, blank=False, null=False)
    date = models.DateField()

    def __str__(self):
        return self.author



