from dbtcore.models import Book, Offer, DBTUser
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    """Book serializer serializes books"""
    class Meta:
        model = Book

class DBTUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBTUser

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
