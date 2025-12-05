from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def home(request):
    data=Article.objects.all()
    return render(request,'home.html',{'data':data})

def read(request,pk):
    data=Article.objects.get(id=pk)
    context={'article':data}
    return render(request,'read.html',context)

def about(request):
    return render(request,'about.html')

