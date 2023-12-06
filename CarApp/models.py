from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    cname= models.CharField(max_length=50)
    phone= models.PositiveIntegerField()
    caddress= models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image1 = models.ImageField(upload_to='ad_images/')
    image2 = models.ImageField(upload_to='ad_images/')
    image3 = models.ImageField(upload_to='ad_images/')
    image4 = models.ImageField(upload_to='ad_images/')
    image5 = models.ImageField(upload_to='ad_images/')
    LOCATION_CHOICES = [
          ('Dhaka', 'Dhaka'),
        ('Chittagong', 'Chittagong'),
        ('Rajshahi', 'Rajshahi'),
        ('Sylhet', 'Sylhet'),
        ('Khulna', 'Khulna'),
        ('Barisal', 'Barisal'),
        ('Rangpur', 'Rangpur'),
        # Add more choices as needed
    ]

    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    def __str__(self):
        return self.title



class UserCar(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    client_name = models.CharField(max_length=100)
    client_mobile = models.CharField(max_length=20)
    client_address = models.TextField()
    car_problem = models.TextField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.client_name}'s {self.car_name} {self.car_model}"



class Contact(models.Model):
    name = models.CharField(max_length=122)
    email =models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
            return self.name