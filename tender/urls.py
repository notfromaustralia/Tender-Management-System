from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('<int:tenderID>', views.tender_details, name='tender'),
    path('', views.tender_list, name='tenders'),
]