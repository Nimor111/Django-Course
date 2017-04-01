from django.contrib import admin
from .models import BlogPost, Comment, Tag


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'created_at', 'updated_at', 'content'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
