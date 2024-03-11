from django.shortcuts import render
from tender.models import Category

# Create your views here.
def index(request):
    tender_categories=Category.objects.all()
    context ={
        'TenderCategories': tender_categories,
    }
    return render(request, 'webpage/index.html', context)
 