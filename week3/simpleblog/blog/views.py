from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogPost, Tag, Comment


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
    if request.method == 'POST':
        # import ipdb; ipdb.set_trace()
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.get('tags').split(',')

        b = BlogPost.objects.create(title=title, content=content)

        for tag in tags:
            if not Tag.objects.filter(name=tag):
                t = Tag.objects.create(name=tag)
                b.tags.add(t)
            else:
                b.tags.add(Tag.objects.get(name=tag))

        b.save()

    return render(request, 'add_post.html', locals())
