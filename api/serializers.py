from django.contrib.auth.models import User
from dbtcore.models import Book, Offer
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    """Book serializer serializes books"""
    class Meta:
        model = Book

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
