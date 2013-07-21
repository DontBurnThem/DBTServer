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
        A view that returns a set of offers based on some parameters.
    """

    http_method_names = ['get',]

    def get(self, request, format=None):
        """
        Return a list of all offers for the given isbn
        """
        data = Offer.objects.all()
        if 'radius' in request.QUERY_PARAMS:
            if 'll' not in request.QUERY_PARAMS: return Response(status=400)
            ll = [ float(x) for x in request.QUERY_PARAMS['ll'].split(',') ]
            if len(ll) != 2: return Response(status=400)
            data = Offer.local_objects.get_local(ll, float(request.QUERY_PARAMS['radius']))

        if 'isbn' in request.QUERY_PARAMS:
            data = data.filter(book__isbn__contains=request.QUERY_PARAMS['isbn'])

        serializer = OfferSerializer(data, many=True)
        return Response(serializer.data)
