from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import SignUpForm, UserCreationForm
from .models import SiteUser
from tender.models import Category,Tender

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            company_name = form.cleaned_data.get('company_name')
            mobile_number = form.cleaned_data.get('mobile_number')
            address = form.cleaned_data.get('address')
            SiteUser.objects.create(user=user, company_name=company_name, mobile_number=mobile_number, address=address)
            messages.success(request, 'Account Created')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # You might want to handle user creation logic here
            return render(request, 'auth/signup.html')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')  # Assuming 'dashboard' is the name of the URL pattern for the dashboard page
        else:
            messages.error(request, 'Invalid credentials')  # Tagging the message as an error
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')

def logout(request):
    tender_categories=Category.objects.all()
    context ={
        'TenderCategories': tender_categories,
    }
    auth_logout(request)
    messages.success(request, 'You are now logged out')
    return render(request, 'webpage/index.html',context)

def dashboard(request):
    tenders=Tender.objects.all()
    context ={
        'Tenders': tenders,
    }
    return render(request,'auth/dashboard.html',context)
