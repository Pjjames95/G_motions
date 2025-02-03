from django.db import models

class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    property_1 = models.CharField(max_length=50)
    property_2 = models.CharField(max_length=50)
    description = models.TextField()
    short_description = models.CharField(max_length=400)
    car_image_url = models.URLField(max_length=200, default='default_image.png')  # Changed to URLField
    car_image2_url = models.CharField(max_length=255, default='default_image.png')  # Change the value as necessary)  # Changed to URLField

    def __str__(self):
        return self.car_name

class AdminMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Message from {self.name}'
