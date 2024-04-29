from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('<int:tenderID>', views.tender_details, name='tender'),
    path('edit/<int:tenderID>', views.edit_tender, name='edit-tender'),
    path('search', views.search, name='search'),
    path('', views.tender_list, name='tenders'),
    path('create', views.tender_create, name='create_tender'),
    path('published', views.published_tenders, name='published_tenders'),
]