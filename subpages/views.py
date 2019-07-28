from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Content_with_1_image
from .models import Photo
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
