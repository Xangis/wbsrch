from django.contrib import admin
from blog.models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'published', 'visible')

admin.site.register(BlogPost, BlogPostAdmin)
