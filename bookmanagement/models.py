# -*- coding:utf-8 -*-
from django.db import models
from utils.countryEnum import countryEnumTuple
from django.core.urlresolvers import reverse

class Author(models.Model):
    COUNTRY_ENUM = countryEnumTuple()
    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    Age = models.IntegerField()
    Country = models.CharField(max_length=128,choices=COUNTRY_ENUM)

    class META:
        ordering = ['Name']

    def __unicode__(self):
        return self.Name


class Book(models.Model):
    ISBN = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=128)
    Author = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=128)
    PublishDate = models.DateField()
    Price = models.DecimalField(max_digits=19,decimal_places=2) # one billion with 2 decimal number

    class META:
        ordering = ['Title']

    def get_absolute_url(self):
        return reverse("Book.views.details", args=[str(self.ISBN)])

    def __unicode__(self):
        return self.Title
