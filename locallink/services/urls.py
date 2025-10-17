from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/create/', views.create_service, name='create_service'),
    path('services/<int:pk>/update/', views.update_service, name='update_service'),
    path('services/<int:pk>/delete/', views.delete_service, name='delete_service'),
    path('category/<int:category_id>/', views.category_services, name='category_services'),
]
