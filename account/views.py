from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .models import Addresses
from .forms import LoginForm, UserRegistrationForm, AddNewAddress

def user_login(request):
    if request.method != 'POST':
        login_form = LoginForm()
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    return HttpResponse("Account disabled")
            else:
                return HttpResponse("Invalid Login")
    
    return render(request, 'account/login.html', {'login_form': login_form})


def register(request):
    if request.method != 'POST':
        register_form = UserRegistrationForm()

    else:
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid:
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()

    return render(request, 'account/register.html', {"register_form": register_form})




def all_address(request):
    address = Addresses.objects.all()

    return render(request, 'account/address.html', {'address': address})


def particular_address(request, address_id):
    '''Retreving a single user address from db'''
    address = Addresses.objects.get(id=address_id)
    print(address)

    return render(request, 'account/particular_address.html', {'address': address})


def create_address(request):
    if request.method != 'POST':
        form = AddNewAddress()
    else:
        form = AddNewAddress(request.POST)
        if form.is_valid:
            new_address = form.save(commit=False)
            new_address.user = request.user
            form.save()

    return render(request, 'account/create_address.html', {'form': form})