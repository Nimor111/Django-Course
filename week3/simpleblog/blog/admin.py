from django.contrib import admin

from .models import BlogPost, Tag, Comment


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )

    def __str__(self):
        return self.name


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'content', 'created_at')
