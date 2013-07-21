from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from math import asin

class LocalOfferManager(models.Manager):
    def get_local(self, point, distance):
        """This method returns a queryset returning only local results

        :point: a 2-tuple of (latitude, longitude) of the search center
        :distance: The search distance in kilometers.
        :returns: a pre-filtered queryset with local results only

        """
        d_alpha = asin(distance/20037.0) #Get angle from distance 20037 is the
        # Earth radius. The above formula approximates the arc with a triangle
        # side. Could be better, could be worse. It works quite fine for small
        # distances.
        return super(LocalOfferManager, self).get_query_set(
                ).filter(lat__range=(point[0]-d_alpha,point[0]+d_alpha)
                ).filter(lon__range=(point[1]-d_alpha,point[1]+d_alpha))

class DBTUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """@todo: Docstring for create_user.

        :email: @todo
        :password: @todo
        :returns: @todo

        """
        u = DBTUser()
        u.email = email
        u.set_password(password)
        u.save()

    def create_superuser(self, email, password):
        """@todo: Docstring for create_superuser.

        :email: @todo
        :password: @todo
        :returns: @todo

        """
        u = DBTUser()
        u.email = email
        u.set_password(password)
        u.save()

class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13)

    def __unicode__(self):
        return "Book ISBN: " + self.isbn

class DBTUser(AbstractBaseUser):
    email = models.EmailField(unique=True, db_index=True)
    books = models.ManyToManyField(Book, through='Offer')

    USERNAME_FIELD = 'email'

    objects = DBTUserManager()

    def is_active(self):
        return True

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
    user = models.ForeignKey(DBTUser)
    book = models.ForeignKey(Book)

    objects = models.Manager()
    local_objects = LocalOfferManager()

    def __unicode__(self):
        return "Book ISBN: " + self.book.isbn + " for " + str(self.price) + " credits."
