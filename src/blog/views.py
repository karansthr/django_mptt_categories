from django.shortcuts import render , get_object_or_404
from .models import Post , Category

def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()
    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        instance = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        instance = get_object_or_404(Post, slug = category_slug[-1])
        return render(request, "post_detail.html", {'instance':instance})
    else:
        return render(request, 'categories.html', {'instance':instance})

def post_detail(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    return render(request,"post_detail.html",{ 'instance':instance})


def post_list(request,slug=None):
    posts = Post.objects.all()
    return render(request,"post_list.html",{ 'posts':posts})
