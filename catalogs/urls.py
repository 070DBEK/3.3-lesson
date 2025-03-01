from django.urls import path
from .views import catalog_list, catalog_detail


urlpatterns = [
    path('', catalog_list, name='catalog-list'),
    path('<int:pk>/', catalog_detail, name='catalog-detail'),
]