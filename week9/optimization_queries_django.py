# select all foreign key objects in one query and then all the many to many objects,
# using intermediate table
posts = Post.objects.select_related('user').prefetch_related('tags').all()
