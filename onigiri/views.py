from django.http import Http404
from django.shortcuts import render
from directory.forms import SearchForm

def home(request):
    searchform = SearchForm()
    return render(request, 'onigiri/index.html', {'searchform' : searchform})
