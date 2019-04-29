from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)

class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=32)
    price = models.IntegerField(verbose_name='价格', max_length=5)

