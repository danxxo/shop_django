from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/add/', views.create_product, name='create_product'),
    path('shop/add/category', views.create_category, name='create_category'),
    path('shop/add/csv', views.upload_csv, name='upload_csv'),
    
]