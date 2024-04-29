from django.shortcuts import render
from tender.models import Category, Tender
from django.db.models import Count

# Create your views here.


def index(request):
    categories = Category.objects.annotate(item_count=Count("id"))
    # for obj in category_list:

    context = {
        'categories': categories,
    }
    return render(request, 'webpage/index.html', context)
