from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms.models import inlineformset_factory

from directory.models import Series, Volume, Chapter
from directory.forms import SeriesVolumeFormSet

class SeriesListView(ListView):
    model = Series

class SeriesDetailView(DetailView):
    model = Series

class SeriesCreate(CreateView):
    model = Series
    template_name = "directory/form.html"
    fields = ['title', 'author', 'artist']

def series_edit(request, pk=None):
    series = get_object_or_404(Series, pk=pk)
    SeriesInlineFormSet = inlineformset_factory(Series, Volume, fields=('title','number'))
    if request.method == "POST":
        formset = SeriesInlineFormSet(request.POST, instance=series)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(series.get_absolute_url())
    else:
        formset = SeriesInlineFormSet(instance=series)
    return render_to_response("directory/series-form.html", {
        "formset": formset,
    })

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

    def get_initial(self):
        if self.request.method == 'GET' and 's' in self.request.GET:
            series = get_object_or_404(Series, pk=self.request.GET['s'])
            return {
                'series':series,
            }
        else:
            return None

class VolumeUpdate(UpdateView):
    model = Volume
    template_name = "directory/form.html"
    fields = ['title', 'number', 'series']

class VolumeDelete(DeleteView):
    model = Volume
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

class ChapterCreate(CreateView):
    model = Chapter
    template_name = "directory/form.html"
    fields = ['title', 'number', 'volume']

    def get_initial(self):
        if self.request.method == 'GET' and 'v' in self.request.GET:
            volume = get_object_or_404(Volume, pk=self.request.GET['v'])
            return {
                'volume':volume,
            }
        else:
            return None

class ChapterUpdate(UpdateView):
    model = Chapter
    template_name = "directory/form.html"
    fields = ['title', 'number', 'volume']

class ChapterDelete(DeleteView):
    model = Chapter
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

def title(request):
    pass