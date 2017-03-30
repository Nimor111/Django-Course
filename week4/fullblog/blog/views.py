from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def post_list_view(request):
    posts = BlogPost.objects.all()

    return render(request, 'website/home-blog-v4.html', locals())


@login_required(login_url='/login/')
def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = len(post.comment_set.all())

    return render(request, 'website/blog-post.html', locals())


def register_view(request):
    form = UserCreationForm()
    print("METHOD IS", request.method)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            return redirect('blog:index')
        else:
            return redirect('/register/')
    return render(request, 'website/page-user-register-classic.html', locals())
