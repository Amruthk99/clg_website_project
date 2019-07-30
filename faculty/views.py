from django.http import HttpResponse
from django.shortcuts import render
from .models import CSE, ECE

# Create your views here.

def home(request):
    cse = CSE.objects
    ece = ECE.objects
    args = {'cse':cse,'ece':ece,}
    return render(request,'faculty.html',args)


def detail(request,page_id):
    args = {'content':'content',}
    return render(request,'subpage.html',args)
