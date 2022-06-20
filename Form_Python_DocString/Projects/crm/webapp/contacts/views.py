from ctypes import addressof
from django.shortcuts import redirect, render
from api.crm import User, get_all_users

# Create your views here.


def index(request):
    return render(request, 'contacts/index.html', {'users': get_all_users()})


def add_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    address = request.POST.get("address")
    phone = request.POST.get("phone")

    user = User(first_name=first_name, last_name=last_name,
                address=address, phone_number=phone)
    user.save()
    return redirect('index')


def delete_contact(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    user = User(first_name=first_name, last_name=last_name)
    user.delete()
    return redirect('index')
