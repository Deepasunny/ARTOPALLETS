from django.db import models

# Create your models here.
class Customisation(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    emailid = models.CharField(max_length=200)
    suggestion = models.TextField()


class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='images/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self .title 

 
 
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phonenumber = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name
    