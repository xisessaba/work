from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'applications', views.ApplicationsViewSet)
router.register(r'brand',views.BrandViewSet )
router.register(r'category', views.CategoryViewSet)


app_name = "shop"

urlpatterns = [
    path('', include(router.urls)),


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

    path('sales/', views.SaleViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        
        }
    ), name = 'sales'),

    path('sales/<int:pk>/', views.SaleViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'sales'),

    path('brand/', views.BrandViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',

        }
    ), name = 'brand'),

    path('brand/<int:pk>/', views.BrandViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'brand'),

    path('category/', views.CategoryViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',

        }
    ), name = 'category'),

    path('category/<int:pk>/', views.CategoryViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'category'),

    path('product_color', views.ProductColorViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',

        }
    ), name = 'product_color'),

    path('product_color/<int:pk>/', views.ProductColorViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'product_color'),

    path('applications', views.ApplicationsViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',

        }
    ), name = 'applications'),

    path('applications/<int:pk>/', views.ApplicationsViewSet.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update',

        }
    ), name = 'applications'),

    
    

]
