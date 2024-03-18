from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('<int:tenderID>', views.tender_details, name='tender'),
    path('', views.tender_list, name='tenders'),
    path('create', views.tender_create, name='create_tender'),
    path('published', views.published_tenders, name='published_tenders'),
    path('<int:tenderID>/bid', views.tender_bid, name='tender_bid'),
]