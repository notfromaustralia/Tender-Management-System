from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [  
    path('history', views.bid_history, name='bid_history'),

]