from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<slug:slug>', views.single_post, name='single-post'),
    path('contact-us', views.contact, name='contact'),
    path('search', views.search, name='search')
]