from django.urls import path, re_path, register_converter
from . import views
from . import convertors


register_converter(convertors.FourDigitsYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),  # основна головна сторінка
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),

    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
