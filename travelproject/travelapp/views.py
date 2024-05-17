from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Staff


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    objs = Staff.objects.all()
    return render(request, "index.html", {'result': obj, 'sresult': objs})
