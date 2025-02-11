from django.shortcuts import render, get_object_or_404, redirect
from .models import POST
from .forms import PostForm

# Vue pour lister les articles
def post_list(request):
    posts = POST.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Vue pour afficher un article en détail

def post_details(request, id):
    post = get_object_or_404(POST, pk=id)
    return render(request, 'blog/post_details.html', {'post': post})

# Vue pour créer un nouvel article
def ajout_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/ajout_post.html', {'form': form})