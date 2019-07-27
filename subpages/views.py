from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Content_with_1_image
from .models import Photo,CSE_Faculty,ECE_Faculty
# Create your views here.

def aboutIIITT(request):
    content = Content_with_1_image.objects.all
    args = {'content':content,}
    return render(request,'profile.html',args)

def detail(request,page_id):
    content = Content_with_1_image.objects.get(title = page_id)
    args = {'content':content,}
    return render(request,'subpage.html',args)

def gallery(request):
    content = Photo.objects.all
    args = {'content':content,}
    return render(request,'subpage.html',args)

def faculty(request):
    cse_faculty = CSE_Faculty.objects.all
    ece_faculty = ECE_Faculty.objects.all
    args = {'cse_faculty':cse_faculty,'ece_faculty':ece_faculty,}
    return render(request,'faculty.html',args)
