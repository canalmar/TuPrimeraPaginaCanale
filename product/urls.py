from django.urls import path
from . import views

app_name = 'product'  

urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    path('list/', views.product_list, name='product_list'),
]