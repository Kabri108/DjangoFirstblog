
from django.shortcuts import render
from blog.models import Post
# Create your views here.

def blogpage(request):
    allPost=Post.objects.all()
    context={'allPost':allPost}
    return render(request,'blog/blogpage.html',context)

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    allpost=Post.objects.all()
    context={'post':post,'allpost':allpost}
    # context={'post1':post1}
    
    return render(request, 'blog/blogpost.html',context)
