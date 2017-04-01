from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import BlogPost, Tag, Comment
from .forms import BlogPostForm


# Create your views here.
def index_view(request):
    posts = BlogPost.objects.all()

    return render(request, 'index.html', locals())


def post_detail_view(request, pk):
    if request.method == 'POST':
        email = request.POST.get('email')
        content = request.POST.get('content')
        c = Comment.objects.create(email=email, content=content)

        c.post = get_object_or_404(BlogPost, pk=pk)
        c.save()

    post = get_object_or_404(BlogPost, pk=pk)
    tags = post.tags.all()
    comments = Comment.objects.filter(post=post)

    return render(request, 'post_detail.html', locals())


def add_post_view(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:index_view'))
    return render(request, 'add_post.html', locals())
