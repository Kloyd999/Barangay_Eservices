from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('request/', views.request_service, name='request_service'),
    path('my/', views.my_requests, name='my_requests'),
    path('<int:pk>/', views.service_detail, name='service_detail'),
    path('<int:pk>/complete/', views.complete_service, name='complete_service'),
    path('<int:pk>/delete/', views.delete_service, name='delete_service'),
]