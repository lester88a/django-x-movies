from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Genre (models.Model):
    name = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return str(self.name)


class Movie (models.Model):
    title = models.CharField(max_length=128,unique=True)
    year = models.IntegerField()
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    votes = models.IntegerField()
    rate = models.FloatField(max_length=4)
    desc = models.CharField(max_length=256,verbose_name='Description',)
    dateadded = models.DateField(default=timezone.now,verbose_name='Date Added')

    def __str__(self):
        return str(self.title + ' ' + str(self.year))


class UserProfileInfo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    user = models.OneToOneField(User)

    #additional field
    profile_pic = models.ImageField(upload_to='profile_pics',verbose_name='Profile Picture',blank=True)
    wechat = models.CharField(max_length=128,unique=True,verbose_name='WeChat',blank=True)
    qq = models.IntegerField(unique=True,verbose_name='QQ',blank=True)
    mobile = models.CharField(max_length=15,unique=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username
