from django.contrib import admin
from .models import Author, Post

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    # slug
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    # Summernote
    summernote_fields = '__all__'
    list_display = [
        'title',
        'date_created',
        'date_updated'
    ]

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
