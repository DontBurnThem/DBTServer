from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=200)
    isbn = models.IntegerField(primary_key = True)

    def __unicode__(self):
        return self.title + " by " + self.author + ", " + self.edition + " edition."

class Offer(models.Model):
    IMBALLATO = 'I'
    LETTO = 'L'
    USURATO = 'U'
    SCRITTO = 'S'
    DANNEGGIATO = 'D'
    STATUS_CHOICES = (
        (IMBALLATO, "Imballato"),
        (LETTO, "Letto"),
        (USURATO, "Usurato"),
        (SCRITTO, "Scritto"),
        (DANNEGGIATO, "Danneggiato"),
    )
    status =  models.CharField(max_length=1, choices=STATUS_CHOICES, default=IMBALLATO)
    price = models.FloatField()
    lat = models.FloatField()
    lon = models.FloatField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return self.book.title + " for " + str(self.price)
