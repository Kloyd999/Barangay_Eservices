from django.urls import path
from authentication import views 

app_name = 'authentication'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
]