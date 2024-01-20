from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from car.models import Car, Category

menu = [{'title': 'about site', 'url_name': 'about'},
        {'title': 'add article', 'url_name': 'add_page'},
        {'title': 'contact', 'url_name': 'contact'},
        {'title': 'login', 'url_name': 'login'}]


data_db = [
    {'id': 1, 'title': 'BMW M5 F90', 'content': '''<h1>The BMW M5 F90</h1> is a powerhouse of performance and luxury, blending the elegance of a sedan with the heart of a high-performance sports car. Released in 2017, it carries on the M5 legacy with a blend of cutting-edge technology, powerful engineering, and dynamic design.
Under the hood, it boasts a twin-turbocharged 4.4-liter V8 engine that produces staggering power, typically around 600 horsepower, with some versions reaching up to 617 horsepower in the M5 Competition. ''',
     'is_published': True},
    {'id': 2, 'title': 'AUDI', 'content': 'bio', 'is_published': False},
    {'id': 3, 'title': 'PORSCHE', 'content': 'bio', 'is_published': True},
    {'id': 4, 'title': 'FERRARI', 'content': 'bio', 'is_published': True},
]

def index(request):
    posts = Car.published.all()

    data = {
        'title' : 'main page',
        'menu' : menu,
        'posts': posts,
        'cat_selected': 0,
    }

    t = render_to_string('car/index.html', context=data)
    return HttpResponse(t)

    # return render(request,'car/index.html' ) # те саме, що зверху

def about(request):
    data = {'title': 'about site', 'menu': menu}
    return render(request, 'car/about.html', data)

def show_post(request, post_slug):
    post = get_object_or_404(Car, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'car/post.html', data)


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)

    return HttpResponse(f"<h1>archive in year : </h1><p> {year}</p>")

def addpage(request):
    return HttpResponse("adding article")

def contact(request):
    return HttpResponse("Contact")

def login(request):
    return HttpResponse("login")

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Car.published.filter(cat_id=category.pk)
    data = {
        'title': f'heading : {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'car/index.html', context=data)
def page_not_found(request, exception):
    return HttpResponseNotFound("<h1> page not found <h1>")