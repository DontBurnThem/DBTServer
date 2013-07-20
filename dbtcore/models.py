from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    isbn = models.IntegerField(primary_key = True)

    def __unicode__(self):
        return "Book ISBN: " + self.isbn

class Offer(models.Model):
    MINT = '1'
    OPENED = '2'
    USED = '3'
    WRITTEN = '4'
    DAMAGED = '5'
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
        return self.book.title + " for " + str(self.price)
