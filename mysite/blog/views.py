from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# def post_detail(request, id):
#     try:
#         post =  Post.published.get(id=id) # get returns a single object not a queryset
#     except Post.DoesNotExist:
#         raise Http404("No Post Found.")
    
    # return render(request, 'blog/post/detail.html', {'post' : post })

def post_detail(request, id):
    post  = get_object_or_404(Post, id=id,  status=Post.Status.PUBLISHED)

    return render(request, 'blog/post/detail.html', {'post': post})