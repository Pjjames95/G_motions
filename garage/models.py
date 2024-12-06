from django.db import models

class Garage_services(models.Model):
    garage_name = models.CharField(max_length=50)
    garage_location = models.CharField(max_length=100)
    garage_image = models.ImageField(upload_to='garages/')
    garage_contacts = models.IntegerField(default=0)

    def __str__(self):
        return self.garage_name

class ComplainMessage(models.Model):
    message = models.TextField()
    email = models.EmailField()

