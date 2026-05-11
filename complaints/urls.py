from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('<int:pk>/', views.complaint_detail, name='complaint_detail'),
]