from django.contrib import admin
from .models import Post, tags, Follow
# Register your models here.
admin.site.register(Post)
admin.site.register(tags)
admin.site.register(Follow)
