from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:id>', views.product_detail, name='product_detail')
]

