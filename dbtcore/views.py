# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from dbtcore.models import Offer

def searchbyisbn(request):
    return render_to_response("dbtcore/searchbyisbn.html")

def showoffers(request):        # tolto isbn
    result_list = Offer.objects.all() # tried to change the test, got past this error
    return render_to_response("dbtcore/showoffers.html", {"list": result_list})
