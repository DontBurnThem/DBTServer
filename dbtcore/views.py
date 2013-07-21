# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from dbtcore.models import Offer

from django.contrib.auth import login
from django.shortcuts import redirect
from social_auth.decorators import dsa_view

def searchbyisbn(request):
    return render_to_response("dbtcore/searchbyisbn.html")

def showoffers(request):        # tolto isbn
    result_list = Offer.objects.all() # tried to change the test, got past this error
    return render_to_response("dbtcore/showoffers.html", {"result_list": result_list})

@dsa_view()
def register_by_access_token(request, backend, *args, **kwargs):
    access_token = request.GET.get('access_token')
    user = backend.do_auth(access_token)
    if user and user.is_active:
        login(request, user)
    return redirect('/error/')        # change the destination

