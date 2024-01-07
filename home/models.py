from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_description = models.TextField()
    description = models.TextField()


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill')
    title = models.CharField(max_length=500, verbose_name='نام')
    percent = models.SmallIntegerField(verbose_name='درصد مهارت')

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact')
    instagram = models.URLField(verbose_name='اینستاگرام')
    telegram = models.URLField(verbose_name='تلگرام')
    phone = models.CharField(max_length=11, verbose_name='تلفن')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    country = models.CharField(max_length=500, verbose_name='کشور')
    state = models.CharField(max_length=500, verbose_name='استان')
    city = models.CharField(max_length=500, verbose_name='شهر')
    map = models.URLField(verbose_name='مکان')

    def __str__(self):
        return self.user.username
