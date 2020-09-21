from django.contrib import admin

# Register your models here.

from .models import BlogPost, AboutMePost

class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ['title', 'dateCreated', 'datePublished', ]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(AboutMePost)
