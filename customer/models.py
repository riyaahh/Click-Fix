from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])



    def __str__(self):
        return str(self.user.username.__str__())
    
# class login(models.Model):
#     username = models.CharField(max_length=50,unique=True)
#     password = models.CharField(max_length=50)


#     def __str__(self):
#         return str(self.username.__str__())



