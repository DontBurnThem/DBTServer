from core.models import User, Book, Offer
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    """Book serializer serializes books"""
    class Meta:
        model = Book

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
