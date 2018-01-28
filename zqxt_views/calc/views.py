from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))
	pass
# Create your views here.
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
 	return render(request,'home.html')