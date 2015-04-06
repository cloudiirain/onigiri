from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from directory.models import Series, Volume, Chapter
from directory.forms import SeriesForm

class SeriesListView(ListView):
    model = Series

class SeriesDetailView(DetailView):
    model = Series

class SeriesCreate(CreateView):
    model = Series
    fields = ['title', 'author', 'artist']

class SeriesUpdate(UpdateView):
    model = Series
    fields = ['title', 'author', 'artist']

class SeriesDelete(DeleteView):
    model = Series
    success_url = reverse_lazy('series-list')

def editseries(request):
    pass

def editvolume(request):
    pass

def editchapter(request):
    pass

def title(request):
    pass