from django.http import HttpResponse
from django.shortcuts import render
from .models import SubPageContent
# Create your views here.

def aboutIIITT(request):
    content = SubPageContent.objects
    return render(request,'subpage.html',{'content':content})
