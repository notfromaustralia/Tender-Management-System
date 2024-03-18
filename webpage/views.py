from django.shortcuts import render
from tender.models import Category, Tender

# Create your views here.
def index(request):
    category_name = request.GET.get('name',None)
    tender_categories=Category.objects.all()
    if category_name is not None:
        tenderByCategoryLength = Tender.objects.filter(category = category_name).count()
    else:
        tenderByCategoryLength = 0
    context ={
        'TenderCategories': tender_categories,
        'TendersCount': tenderByCategoryLength
    }
    return render(request, 'webpage/index.html', context)
