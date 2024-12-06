from django.db import models


class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    property_1 = models.CharField(max_length=50)
    property_2 = models.CharField(max_length=50)
    description = models.TextField()
    short_description = models.CharField(max_length=400)
    car_image = models.ImageField(upload_to='cars/')
    car_image2 = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.car_name

class AdminMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Message from {self.name}'
