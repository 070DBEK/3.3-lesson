from django.urls import path
from .views import order_list, order_detail


urlpatterns = [
    path('', order_list, name='order-list'),
    path('<int:pk>/', order_detail, name='order-detail'),
]
