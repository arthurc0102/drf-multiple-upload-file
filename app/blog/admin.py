from django.contrib import admin

from .models import Post, Attachment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_at', 'update_at')
    list_filter = ('create_at', 'update_at')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'file')
    list_filter = ('post',)
