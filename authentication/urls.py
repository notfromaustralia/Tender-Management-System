from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.signup, name='register'),
    path('create-user', views.createUser, name='create-user'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
