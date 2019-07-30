from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import CSE, ECE

# Create your views here.

def home(request):
    cse = CSE.objects
    ece = ECE.objects
    args = {'cse':cse,'ece':ece,}
    return render(request,'faculty.html',args)


def detailie(request,id):

    content = ECE.objects.get(title = id)
    return render(request,'profile.html',{'content':content})
