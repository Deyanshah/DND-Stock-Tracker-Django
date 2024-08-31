from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('update_quant/',views.update_quant,name='update_quant'),
    path('admin_page/',views.admin,name='admin'),
    path('display_quant/', views.display_quant, name='display_quant'),
    # path('red_adjust_stock_ad/', views.red_adjust_stock_ad, name='product_1'),
]
