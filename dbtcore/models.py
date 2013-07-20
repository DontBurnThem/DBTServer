from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.IntegerField(primary_key = True)

    def __unicode__(self):
        return "Book ISBN: " + str(self.isbn)

class Offer(models.Model):
    MINT = '0'
    OPENED = '1'
    USED = '2'
    WRITTEN = '3'
    DAMAGED = '4'
    STATUS_CHOICES = (
        (MINT, "Mint"),
        (OPENED, "Read"),
        (USED, "Used"),
        (WRITTEN, "Written"),
        (DAMAGED, "Damaged"),
    )
    status =  models.CharField(max_length=1, choices=STATUS_CHOICES, default=MINT)
    price = models.FloatField()
    lat = models.FloatField()
    lon = models.FloatField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __unicode__(self):
        return str(self.book.isbn) + " for " + str(self.price)
