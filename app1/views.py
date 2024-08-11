from django.shortcuts import render
from app1.models import *

# Create your views here.
def homeV(request):
    results=Book.objects.all()
    return render(request,'home.html',{'books':results})

def createAuthor(request):
    if request.method=="POST":
        name=request.POST.get('aname')
        age=request.POST.get('age')
        rating=request.POST.get('rate')
        obj=Author(name=name,age=age,rating=rating)
        obj.save()
        print(name,age,rating)
    return render(request,'author.html')

def createBook(request):
    if request.method=="POST":
        t=request.POST.get('bname')
        p=request.POST.get('price')
        g=request.POST.get('genre')
        s=request.POST.get('sno')
        im=request.FILES.get('img')
        caption=request.POST.get('cap')
        if Author.objects.filter(id=s).exists():
            a=Author.objects.get(id=s)
            obj=Book(title=t,price=p,genre=g,author=a,pic=im,cap=caption)
            obj.save()
    return render(request,'book.html')