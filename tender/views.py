from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tender, Category
from .forms import TenderForm

# Create your views here.
def tender_list(request):
    all_tenders = Tender.objects.all()
    context={
        'Tenders': all_tenders
    }
    return render(request,'tenders/tenders.html',context)

@login_required
def tender_details(request, tenderID):
    tender=get_object_or_404(Tender, pk=tenderID)
    context ={
        'Tender':tender
    }
    return render(request,'tenders/tender.html',context)

@login_required
def tender_create(request):
    context ={
                'TenderCategories': Category.objects.all(),
                'TenderForm': TenderForm()
            }
    if request.method=='POST':
        tender_form = TenderForm(request.POST, request.FILES)
        if tender_form.is_valid():
            createdTender = tender_form.save(commit=False)
            createdTender.publisher = request.user
            createdTender.save()
            
            messages.success(request, 'Tender created')
            return render(request,'tenders/create.html',context)
        else:
            messages.error(request, 'Failed to create tender')
            return render(request,'tenders/create.html',{
             'TenderCategories': Category.objects.all(),
             'TenderForm': tender_form
        })
    else:
        return render(request,'tenders/create.html',context)
    
@login_required
def published_tenders(request):
    owner = request.user
    tendersByOwner = Tender.objects.filter(publisher = owner)
    return render(request,'tenders/published-tenders.html',{
             'TendersByOwner': tendersByOwner
        })
