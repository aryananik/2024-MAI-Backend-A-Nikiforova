from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurants, name='restaurants'),
    path('menu/<int:restaurant_id>/', views.menu, name='menu'),
    path('order/create/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('order/<int:order_id>/update/', views.update_order, name='update_order'),
]