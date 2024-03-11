from django.shortcuts import get_object_or_404, render
from .models import Tender

# Create your views here.
def tender_list(request):
    all_tenders = Tender.objects.all()
    context={
        'Tenders': all_tenders
    }
    return render(request,'tenders/tenders.html',context)

def tender_details(request, tenderID):
    tender=get_object_or_404(Tender, pk=tenderID)
    context ={
        'Tender':tender
    }
    return render(request,'tenders/tender.html',context)