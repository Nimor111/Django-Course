from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import BlogPostModelForm


def post_list_view(request):
    # import ipdb; ipdb.set_trace()
    public_posts = list(BlogPost.objects.get_public_posts())
    private_posts = list(BlogPost.objects.get_private_posts())

    if request.user.is_authenticated():
        posts = public_posts + private_posts
    else:
        posts = public_posts

    return render(request, 'website/home-blog-v4.html', {'posts': posts})


@login_required(login_url=reverse_lazy('login'))
def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = len(post.comment_set.all())

    return render(request, 'website/blog-post.html', locals())


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            return redirect(reverse_lazy('blog:index'))
        else:
            return redirect('/register/')
    return render(request, 'website/page-user-register-classic.html', locals())


@login_required(login_url=reverse_lazy('login'))
def create_blog_post_view(request):
    form = BlogPostModelForm()

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(reverse_lazy('blog:index'))

    return render(request, 'website/add-blog-post.html', locals())
