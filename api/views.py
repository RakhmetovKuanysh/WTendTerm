from django.http import JsonResponse, QueryDict
from blog.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def blog_list(request):
    try:
        if request.method == "GET":
            blogs = Blog.objects.filter(is_active=True)

            blogs_json = [blog.full() for blog in blogs]            
            return JsonResponse(blogs_json, safe=False)

        elif request.method == "POST":
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            date = datetime.datetime.now()

            blog = Blog.objects.add_blog(title=title, content=content, date=date)

            return JsonResponse(blog.full(), status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(is_active=True, pk=blog_id)

        if request.method == "GET":
            return JsonResponse(blog.full(), status=200)

        elif request.method == "PUT":
            data = QueryDict(request.body)
            blog.title = data.get('title', blog.title)
            blog.content = data.get('content', blog.content)

            blog.save()

            return JsonResponse(blog.full(), status=200)

        elif request.method == "DELETE":
            blog.is_active = False
            blog.save()

            return JsonResponse(blog.full(), status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
