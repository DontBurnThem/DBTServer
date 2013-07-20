# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from core.models import Offer

def searchbyisbn(request):
    return render_to_response("core/searchbyisbn.html")

def showoffers(request, isbn):
    result_list = Offer.objects.filter(book.isbn = isbn)
    return render_to_response(“core/showoffers.html”, {“list”: result_list})
