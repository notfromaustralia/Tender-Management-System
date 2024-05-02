from django.shortcuts import render
from authentication.models import SiteUser
from tender.models import Category, Tender
from django.db.models import Count

# Create your views here.


def index(request):
    categories = Category.objects.annotate(item_count=Count("tender"))
    siteuser = "SiteUser.objects.get(user=request.user.id)"
    context = {
        'categories': categories,
        'siteuser': siteuser,
    }
    return render(request, 'webpage/index.html', context)

