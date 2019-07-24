from django.http import HttpResponse
from django.shortcuts import render
from .models import Image
# Create your views here.

def home(request):
    jobs = Image.objects
    return render(request,'index.html',{'jobs':jobs})
def detail(request,page_id):
    content = get_object_or_404(SubPageContent,pk=page_id)
    args = {'content':content,}
    return render(request,'subpage.html',args)
