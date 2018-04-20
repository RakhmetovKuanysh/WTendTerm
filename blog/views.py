from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
import datetime


def index(request):
    blog_list = Blog.objects.filter(is_active=True)

    context = {
        'blog_list': blog_list,
    }
    return render(request, 'index.html', context)


def new_blog(request):
    return render(request, 'new_blog.html')


def add_blog(request):
    title = request.POST["title"]
    content = request.POST["content"]
    date = datetime.datetime.now()

    if title == "" or content == "":
        return HttpResponseRedirect(reverse('index', args=()))

    obj = Blog.objects.add_blog(title=title, content=content, date=date)
    return HttpResponseRedirect(reverse('index', args=()))


def delete_blog(request, blog_id):
    try:
        blog = Blog.objects.get(is_active=True, pk=blog_id)

        blog.is_active = False
        blog.save()

        return HttpResponseRedirect(reverse('index', args=()))

    except Exception as e:
        return HttpResponseRedirect(reverse('index', args=()))


def detail_blog(request, blog_id):
    try:
        blog = Blog.objects.get(is_active=True, pk=blog_id)

        context = blog.full()

        return render(request, 'detail.html', context)

    except Exception as e:
        print(str(e))
        return HttpResponseRedirect(reverse('index', args=()))


def edit_blog(request, blog_id):
    try:
        blog = Blog.objects.get(is_active=True, pk=blog_id)

        blog.title = request.POST.get("title", blog.title)
        blog.content = request.POST.get("content", blog.content)
        blog.save()

        return HttpResponseRedirect(reverse('index', args=()))

    except Exception as e:
        return HttpResponseRedirect(reverse('index', args=()))
