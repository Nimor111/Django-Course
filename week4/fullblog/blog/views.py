from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def post_list_view(request):
    posts = BlogPost.objects.all()

    return render(request, 'website/home-blog-v4.html', locals())


def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = len(post.comment_set.all())

    return render(request, 'website/blog-post.html', locals())
