from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [  
    path('history', views.bid_history, name='bid_history'),
    path('incoming', views.bid_incoming, name='bid_incoming'),
    path('application/<int:tenderID>', views.tender_bid, name='bid-application'),
]