from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Tender, Category
from .forms import TenderForm
from django.db.models import Q

# Create your views here.


def tender_list(request):
    all_tenders = Tender.objects.all()
    context = {
        'Tenders': all_tenders
    }
    return render(request, 'tenders/tenders.html', context)

def tenders_by_category(request, categoryID):
    category = get_object_or_404(Category, pk=categoryID)
    tenders = Tender.objects.filter(category=category)
    context = {
        'category': category,
        'CategoryTenders': tenders
    }
    return render(request, 'tenders/tenders-by-category.html', context)

@login_required
def tender_details(request, tenderID):
    tender = get_object_or_404(Tender, pk=tenderID)
    context = {
        'Tender': tender
    }
    return render(request, 'tenders/tender.html', context)


@login_required
def tender_create(request):
    context = {
        'TenderCategories': Category.objects.all(),
        'TenderForm': TenderForm()
    }
    if request.method == 'POST':
        tender_form = TenderForm(request.POST, request.FILES)
        if tender_form.is_valid():
            createdTender = tender_form.save(commit=False)
            createdTender.publisher = request.user
            createdTender.save()

            messages.success(request, 'Tender created')
            return render(request, 'tenders/create.html', context)
        else:
            messages.error(request, 'Failed to create tender')
            return render(request, 'tenders/create.html', {
                'TenderCategories': Category.objects.all(),
                'TenderForm': tender_form
            })
    else:
        return render(request, 'tenders/create.html', context)


@login_required
def published_tenders(request):
    owner = request.user
    tendersByOwner = Tender.objects.filter(publisher=owner)
    return render(request, 'tenders/published-tenders.html', {
        'TendersByOwner': tendersByOwner
    })


@login_required
def edit_tender(request, tenderID):
    tender = Tender.objects.get(id=tenderID)
    form = TenderForm(instance=tender)
    context = {"form": form, "tender": tender}

    if request.method == "GET":
        return render(request, "tenders/published-tenders-edit.html", context)
    elif request.method == "POST":
        form = TenderForm(request.POST, request.FILES, instance=tender)
        if form.is_valid():
            ten = form.save(commit=False)
            ten.save()
            return redirect(reverse_lazy("published_tenders"))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

def search(request):
    if request.method == "POST":
        name = request.POST['searchy']
        tender = Tender.objects.all().filter(Q(title__icontains=name) | Q(tender_no__icontains=name))
        context = {"tender": tender, "search_term":name}
        for ten in tender:
            print(ten.title)
        return render(request, "webpage/search.html", context)
