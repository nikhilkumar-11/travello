
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('dynhome/', views.dynhome, name='dynhome'),
    path('addnum/', views.addnum, name='addnum'),
    path('addnum/add', views.add, name='add'),
    path('travello/', views.travello, name='travello'),
]