from django.db import models


class Author(models.Model):

    AuthorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=128)
    Age = models.IntegerField()
    Country = models.CharField()

    class META:
        ordering = ['Name']

    def __unicode__(self):
        return self.user.username


class Book(models.Model):

    ISBN = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=128)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=128)
    PublishDate = models.DateField()
    Price = models.DecimalField()

    class META:
        ordering = ['Title']

    def __unicode__(self):
        return self.Title


