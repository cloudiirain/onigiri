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
    template_name = "directory/form.html"
    fields = ['title', 'author', 'artist']

class SeriesUpdate(UpdateView):
    model = Series
    template_name = "directory/form.html"
    fields = ['title', 'author', 'artist']

class SeriesDelete(DeleteView):
    model = Series
    context_object_name = "object"
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

class VolumeCreate(CreateView):
    model = Volume
    template_name = "directory/form.html"
    fields = ['title', 'number', 'series']

class VolumeUpdate(UpdateView):
    model = Volume
    template_name = "directory/form.html"
    fields = ['title', 'number', 'series']

class VolumeDelete(DeleteView):
    model = Volume
    context_object_name = "object"
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

def editchapter(request):
    pass

def title(request):
    pass