from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bid
from .forms import BidForm
from tender.models import Tender
# Create your views here.
@login_required
def bid_history(request):
    owner = request.user
    bidsByOwner = Bid.objects.filter(bidder = owner)
    # bidsByOwner = Bid.objects.all()
    return render(request,'bids/bid-history.html',{
             'Bids': bidsByOwner
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
            return render(request, 'bids/bid-application.html', {'Tender': tender, 'BidForm': BidForm()})
        else:
            messages.error(request, 'Request to tender failed')
            return render(request, 'bids/bid-application.html', {'Tender': tender, 'BidForm': bid_form})
    return render(request, 'bids/bid-application.html', {'Tender': tender, 'BidForm': bid_form})
