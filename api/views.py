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

class OfferIsbnSearchView(APIView):
    """
        A view that returns a set of offers based on a parameter.
    """

    http_method_names = ['get',]

    def get(self, request, isbn, format=None):
        """
        Return a list of all offers for the given isbn
        """
        data = Offer.objects.filter(book__isbn=isbn)
        serializer = OfferSerializer(data, many=True)
        return Response(serializer.data)

class OfferGeoSearchView(APIView):
    """
        A view that returns a set of offers based on a parameter.
    """

    http_method_names = ['get',]

    def get(self, request, lat, lon, distance, format=None):
        """
        Return a list of all offers around a point
        """
        import math
        lat, lon, distance = (float(lat), float(lon), float(distance))
        d_alpha = math.asin(distance/20037)
        data = Offer.objects.filter(lon__range=(lon-d_alpha,lon+d_alpha)
                ).filter(lat__range=(lat-d_alpha,lat+d_alpha))
        serializer = OfferSerializer(data, many=True)
        return Response(serializer.data)
