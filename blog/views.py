from django.shortcuts import render

from .forms import PostForm
from .models import Post
# Create your views here.

def index(request):
    Posts=Post.objects.all().order_by('-created_at')
    return render(request, 'blog/listpost.html',{'posts':Posts})


def Ajouterpost(request):
    form= PostForm()
    return render(request, 'blog/ajoupost.html',{'form':form})