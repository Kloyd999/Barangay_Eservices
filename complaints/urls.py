from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('', views.complaint_list, name='complaint_list'),
    path('file/', views.file_complaint, name='file_complaint'),
    path('my/', views.my_complaints, name='my_complaints'),
    path('<int:pk>/', views.complaint_detail, name='complaint_detail'),
    path('<int:pk>/resolve/', views.resolve_complaint, name='resolve_complaint'),
    path('<int:pk>/delete/', views.delete_complaint, name='delete_complaint'),
]