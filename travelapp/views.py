from django.shortcuts import render
from .models import Packages
# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# from .models import userInfo
# Create your views here.
def index(request): 

    pack = Packages.objects.all()

    return render(request,'index.html', {'pack' : pack })

def qrcode(request):
    return render(request, 'qr.html')

def services(request):
    return render(request, 'service.html')

def tourpack(request):
    return render(request, 'package.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')