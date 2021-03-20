from django.db import models

# Create your models here.


def users(models.Model):
    login = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='Login')
    password = models.CharField(max_length=255, null=True,
                                blank=True, verbose_name='Password')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


def UserProfile(models.Model):
    first_name = models.CharField(max_length=255, null=True,
                                  blank=True, verbose_name='First_name')
    last_name = models.CharField(max_length=255, null=True,
                                 blank=True, verbose_name='Last_name')
    user = models.ForeignKey(
        users, on_delete=models.RESTRICT, related_name='user', verbose_name='user')

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


def BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='Name')
    price = models.IntegerField(max_length=255, null=True,
                                blank=True, verbose_name='Price')
    description = models.TextField(max_length=255, null=True,
                                   blank=True, verbose_name='')
    created_at = models.DateField(max_length=255, null=True,
                                  blank=True, verbose_name='Created')

    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'


def Book(models.Model):
    num_pages = models.IntegerField(max_length=255, null=True,
                                    blank=True, verbose_name='Num_pages')
    genre = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='genre')
    BookJournalBase = models.ForeignKey(
        BookJournalBase, on_delete=models.RESTRICT, related_name='BookJournalBase', verbose_name='BookJournalBase')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


def Journal(model.Model):
    type_ = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='Name')
    publisher = models.CharField(max_length=255, null=True,
                                 blank=True, verbose_name='Name')
    BookJournalBase = models.ForeignKey(
        BookJournalBase, on_delete=models.RESTRICT, related_name='BookJournalBase', verbose_name='BookJournalBase')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
