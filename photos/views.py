from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from photos.models import Post


def hello_world(request):
    return render(request, 'hello_world.html', {'current_time': str(datetime.now())

     })


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

