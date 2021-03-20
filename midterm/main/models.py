from django.db import models

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True,
                            blank=True, verbose_name='Name')
    price = models.IntegerField(max_length=255, null=True,
                                blank=True, verbose_name='Price')
    description = models.TextField(max_length=255, null=True,
                                   blank=True, verbose_name='Description')
    created_at = models.DateField(max_length=255, null=True,
                                  blank=True, verbose_name='Created')

    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Bases'


class Book(models.Model):
    num_pages = models.IntegerField(max_length=255, null=True,
                                    blank=True, verbose_name='Num_pages')
    genre = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='genre')
    BookJournalBase = models.ForeignKey(
        BookJournalBase, on_delete=models.RESTRICT, related_name='Books', verbose_name='BookJournalBase')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(models.Model):
    type_ = models.CharField(max_length=255, null=True,
                             blank=True, verbose_name='Name')
    publisher = models.CharField(max_length=255, null=True,
                                 blank=True, verbose_name='Name')
    BookJournalBase = models.ForeignKey(
        BookJournalBase, on_delete=models.RESTRICT, related_name='Journal', verbose_name='BookJournalBase')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
