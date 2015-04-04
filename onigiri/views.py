from django.http import Http404
from django.shortcuts import render

def home(request):
    return render(request, 'onigiri/index.html')
