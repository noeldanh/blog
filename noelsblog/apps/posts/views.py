# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
# Create your views here.


def home(request):
    posts_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page_request_var': page_request_var
    }
    return render(request, 'posts/home.html', context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.errors:
        messages.error(request, "Not Successfully Created!")
    elif form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('my_post:home')
    return render(request, 'posts/post_create.html', context)


def post_details(request, post_id):
    context = {
        'post': get_object_or_404(Post, pk=post_id)
    }
    return render(request, 'posts/post_details.html', context)


def post_update(request, post_id):
    instance = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        print form.cleaned_data.get('title')
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated!")
        return redirect('my_post:home')
    context = {
        'instance': instance,
        'form': form,
    }
    return render(request, 'posts/post_update.html', context)


def post_delete(request, post_id):
    instance = get_object_or_404(Post, pk=post_id)
    instance.delete()
    return redirect('my_post:home')
