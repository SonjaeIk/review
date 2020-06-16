from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from research.models import Post
from django.shortcuts import render, get_object_or_404


# Create your views here.

# def index(request):
#     return HttpResponse('Hello, world. You are at the polls index')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'research/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'research/post_detail.html', {'post': post})