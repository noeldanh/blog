# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_display_links = ["created_at"]
    list_editable = ['title']
    list_filter = ['created_at']

    search_fields = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
