from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'recipe', 'user', 'status']
    list_filter = ['status']


admin.site.register(Comment, CommentAdmin)
