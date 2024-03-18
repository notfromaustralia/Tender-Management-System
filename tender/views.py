from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tender, Category
from .forms import TenderForm
from bid.forms import BidForm
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

@login_required
def tender_bid(request, tenderID):
    tender = get_object_or_404(Tender, pk=tenderID)
    bid_form = BidForm()  # Move form instantiation outside of conditional block
    if request.method == 'POST':
        bid_form = BidForm(request.POST, request.FILES)
        if bid_form.is_valid():
            new_bid = bid_form.save(commit=False)
            new_bid.tender = tender
            new_bid.bidder = request.user
            new_bid.save()
            tender.save()
            messages.success(request, 'Request to tender submitted')
            return render(request, 'tenders/tender.html', {'Tender': tender, 'BidForm': BidForm()})
        else:
            messages.error(request, 'Request to tender failed')
            return render(request, 'tenders/tender.html', {'Tender': tender, 'BidForm': bid_form})
    return render(request, 'tenders/tender.html', {'Tender': tender, 'BidForm': bid_form})
