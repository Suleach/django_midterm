from django.db import models

# Create your models here.


class Users(models.Model):
    login = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='Login')
    password = models.CharField(max_length=255, null=True,
                                blank=True, verbose_name='Password')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255, null=True,
                                  blank=True, verbose_name='First_name')
    last_name = models.CharField(max_length=255, null=True,
                                 blank=True, verbose_name='Last_name')
    user = models.ForeignKey(
        Users, on_delete=models.RESTRICT, related_name='user_profile', verbose_name='user')

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
