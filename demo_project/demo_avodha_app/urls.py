from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('shop/<int:shop_id>', views.details, name='details'),
    path('add/', views.add_product, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]