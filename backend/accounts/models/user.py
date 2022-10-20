from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.

class User(AbstractUser):

    email=models.EmailField(
        verbose_name="ایمیل",
        unique=True
    )  

    username=models.CharField(
        max_length=100,
        verbose_name="نام کاربری",
        unique=True
    )   


    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربران"


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS=[]
    
    def __str__(self)-> str:
        return self.username
