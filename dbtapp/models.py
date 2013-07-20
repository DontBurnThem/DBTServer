from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    hash = models.CharField(max_length=200)
    fbid = models.IntegerField()
    tel = models.CharField(max_length=200)

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    edition = models.CharField(max_length=200)
    isbn = models.IntegerField(primary_key = True)

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
    user = models.ForeignKey('User')
    book = models.ForeignKey('Book')
        
        
        
        
        
