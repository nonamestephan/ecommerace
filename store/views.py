from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import *


def home(request):
    projects = Project.objects.all()
    return render(request, 'store/index.html', {'projects': projects})


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'store/collections.html', context)


def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html', context)
    else:
        messages.warning(request, 'No such category found')
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.warning(request, 'No such product found')
            return redirect('collections')
    else:
        messages.warning(request, 'No such category found')
        return redirect('collections')
    return render(request, 'store/products/view.html', context)


def about(request):
    return render(request, 'portfolio/about.html', {})


# def all_blogs(request):
#     blogs = Blog.objects.order_by('-date')
#     return render(request, 'blog/all_blogs.html', {'blogs': blogs})
#
#
# def detail(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/detail.html', {'blog': blog})
