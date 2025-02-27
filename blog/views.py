from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import AjouForm
from .models import Post
# Create your views here.

def index(request):
    Posts=Post.objects.all().order_by('-created_at')
    return render(request, 'blog/listpost.html',{'posts':Posts})

def AjouForms(request):
    form = AjouForm()  # ✅ Toujours initialiser le formulaire

    if request.method == 'POST':    #:🥏pour envoiyer des informantion
        form = AjouForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')

    return render(request, 'blog/ajoupost.html', {"form": form})


def modifier_article(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = AjouForm (request.POST, instance= post)
        if form.is_valid():
            form.save()
        return redirect('index2')
    else:
        form = AjouForm (instance= post)
    return render(request, 'blog/modifier_article.html', {'form': form, 'post': post})


def supprimer_article(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('blogs')
    return render(request, 'blog/supprimer_article.html', {'posts': post})