from django.shortcuts import render,get_object_or_404
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
        ozodbek = PostForm(request.POST)
        if ozodbek.is_valid():
            ozodbek.save()
        return HttpResponse(f"ozodbilan qilingan darsdagi post muvofaqiyatli saqlandi😉😉😉!!!")
    
    else:
        ozodbek = PostForm()

    return render(request, 'post_create.html', {'ozodbek':ozodbek})