from django.shortcuts import render,redirect
from app1.models import Article
# Create your views here.
def home1(request):
    news=Article.objects.all()
    return render(request,'home1.html',{'data':news,'management':True})

def addnews(request):

    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        news=Article.objects.create(
            title=title,
            desc=desc
        )
        # return redirect('home')
    return render(request,'addnews.html')

def delete_(request,pk):
    news=Article.objects.get(id=pk)
    news.delete()
    return redirect('home1')

def update(request,pk):
    news=Article.objects.get(id=pk)

    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        news.title=title
        news.desc=desc
        news.save()
        return redirect('home1')
    return render(request,'update.html',{'news':news})
