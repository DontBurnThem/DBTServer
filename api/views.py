from rest_framework import authentication, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import UserSerializer, BookSerializer, OfferSerializer
from dbtcore.models import Book, Offer
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferSearchView(APIView):
    """
        A view that returns a set of offers based on a parameter.
    """

    http_method_names = ['get',]

    def get(self, request, method, key, format=None):
        """
        Return a list of all offers matching a selected criterion.
        """
        objects = Offer.objects.filter(book__isbn=key)
        return Response(objects)
