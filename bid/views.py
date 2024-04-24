from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bid
# Create your views here.
@login_required
def bid_history(request):
    owner = request.user
    bidsByOwner = Bid.objects.filter(bidder = owner)
    # bidsByOwner = Bid.objects.all()
    return render(request,'bids/bid-history.html',{
             'Bids': bidsByOwner
        })