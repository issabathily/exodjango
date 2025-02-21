from  django.shortcuts import render
from  blog.models import Post
def index2(request):
    return render(request, 'index.html')

def getglog(request):
    Posts=Post.objects.all().order_by('-created_at')
    return render(request , 'blog.html',{'posts':Posts})