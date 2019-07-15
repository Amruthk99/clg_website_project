from django.http import HttpResponse
from django.shortcuts import render
from .models import Image
# Create your views here.

def home(request):
    jobs = Image.objects
    return render(request,'index.html',{'jobs':jobs})
