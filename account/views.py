from django import forms

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib import messages, auth

from account.forms import MyRegistrationForm

def login(request):
    redirect_field_name = '/u/account/'

def logout(request):
    messages.success(request, "You have been successfully logged out.")
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for registering. Please log in.")
            return HttpResponseRedirect(reverse('login'))
    else:
        form = MyRegistrationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def dashboard(request):
    pass