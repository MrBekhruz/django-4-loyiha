from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

def home(request):
    # categories = Category.objects.all()
    # post = Post.objects.all()

    categories = Category.objects.all()
    selected_category = request.GET.get("category")

    if selected_category:
        post = Post.objects.filter(category__name = selected_category)

    else:
        post = Post.objects.all()

    context = {
    'post':post,
    'categories':categories,
    'selected_category':selected_category
    }
    return render(request,'index.html',context)

def post_detail(request,pk):
    data = get_object_or_404(Post , pk=pk)
    context = {
        'data':data
    }
    return render(request, 'post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        ozodbek = PostForm(request.POST,request.FILES)
        if ozodbek.is_valid():
            ozodbek.save()
        return redirect('home')
    
    else:
        ozodbek = PostForm()

    return render(request, 'post_create.html', {'ozodbek':ozodbek})


def post_update(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        ozodbek = PostForm(request.POST,request.FILES,instance=post)
        if ozodbek.is_valid():
            ozodbek.save()
            return render('home')
    else:
        ozodbek=PostForm(instance=post)
    context = {
        'ozodbek':ozodbek,
        'post':post
    }
    return render(request,'post_update.html',context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_delete.html', {'post':post})