from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
def index(request):
    blog=Blogpost.objects.all()
    return render(request,'blog/index.html',{'blog':blog})

def blogpost(request,id):
    blog=Blogpost.objects.filter(post_id=id)
    if len(blog)>0:
        return render(request,'blog/blogpost.html',{'blog':blog})
    else:
        return HttpResponse('Oops! Sorry You Are In a Wrong way')