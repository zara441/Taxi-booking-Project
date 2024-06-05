from django.db import models
from django.contrib.auth.models import User



class Customers(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    phone_number=models.BigIntegerField()
    stand_name=models.CharField(max_length=250,null=True)
    vehicle_number=models.CharField(null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"name:{self.name}"
    

