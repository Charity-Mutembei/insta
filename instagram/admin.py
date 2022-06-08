from django.contrib import admin
from .models import Post,Follow, Stream, Profile, Tags
# Register your models here.
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Follow)
admin.site.register(Stream)
admin.site.register(Profile)
