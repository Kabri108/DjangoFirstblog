
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        # phone=request.POST['phone']
        content=request.POST['content']
        contact=Contact(name=name,email=email,content=content)
        contact.save()
        # print(name,content,email)

        if len(name)<2 or len(email)<3 or len(content)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            contact=Contact(name=name,email=email,content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    return render(request,'home/contact.html')    

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPost=Post.objects.none()
    else:    
      allPostTitle=Post.objects.filter(title__icontains=query)
      allPostContent=Post.objects.filter(content__icontains=query) 
      allPost=allPostTitle.union(allPostContent)

    if allPost.count() == 0:
        messages.warning(request,"No search reasult found .Please refine your query")
    params={'allPost':allPost,'query':query}
    return render(request,'home/search.html',params)


def handelSignup(request):
    if request.method == 'POST':
        # get the all parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pas1=request.POST['pas1']
        pas2=request.POST['pas2']

        # check for erroneous inputs

        # create the user
        myuser=User.objects.create_user(username,email,pas1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your account has been sucessfully created")
        return redirect('home')
    else:
        return HttpResponse("404- page not found")