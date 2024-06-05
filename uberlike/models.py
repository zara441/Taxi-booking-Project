from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class VehicleStand(models.Model):
    state=models.CharField(max_length=50,null=True)
    district=models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.IntegerField()
    availability = models.IntegerField()
    description = models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,null=True)
    active=models.BooleanField(default=False)
    near_by=models.CharField(max_length=100)
    img=models.ImageField(upload_to="stand_images/")
    lat=models.FloatField()
    lng=models.FloatField()
    zoom=models.IntegerField(null=True)
    price=models.FloatField(null=True)

    class Meta:
        ordering=('description',)
        verbose_name="vehiclestand"
        verbose_name_plural="vehiclestands"

    def __str__(self):
        return self.description
    
    def get_url(self):
        return reverse('detail',args=[self.slug])


class Location(models.Model):
    location=models.CharField(max_length=250)
    lat=models.FloatField()
    lng=models.FloatField()
    

    
