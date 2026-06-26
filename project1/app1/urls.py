from django.urls import path
from .views import *

urlpatterns= [
    path('index/',index,name='index'),
    path('home/',home,name='home'),
    path('product/',product,name='product'),
    path('about/',about,name='about'),
    path('add_user/',add_user,name='add_user'),
    path('users/',users,name='users'),
    path('update/<int:id>/',update_user,name='update_user'),
    path('delete_user/<int:id>/',delete_user,name='delete_user'),
]