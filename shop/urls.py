from django.contrib import admin
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [

    path('users/', views.UsersViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }
    ), name = 'users'),

    path('users/<int:pk>/', views.UsersViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
        }
    ), name = 'users'),

    path('products/', views.ProductViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',

        }
    ), name = 'products'),

    path('products/<int:pk>/', views.ProductViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'products'),

    # path('', views.index, name = 'home'),
    # path('phones', views.phone_list, name = 'phones'),
    # path('laptops', views.laptop_list, name = 'laptops'),
    # path('rassrochka', views.installment_plan, name = 'installment_plan'),
    


]
