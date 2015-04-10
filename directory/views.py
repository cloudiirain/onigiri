from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

from directory.models import Series, Volume, Chapter, SeriesForm, Tags
from directory.forms import SeriesVolumeFormSet, SeriesTitleFormSet, SearchForm

class SeriesListView(ListView):
    model = Series
    queryset = Series.objects.order_by('slug')

class SeriesDetailView(DetailView):
    model = Series

    def get_object(self):
        object = super(SeriesDetailView, self).get_object()
        object.views += 1
        object.save()
        return object

class SeriesCreate(CreateView):
    model = Series
    template_name = "directory/form.html"
    fields = ['title', 'author', 'artist', 'tags', 'image', 'synopsis']

def series_edit(request, pk=None):
    series = get_object_or_404(Series, pk=pk)
    form = SeriesForm(instance=series, prefix="ser")
    sub_form = SeriesVolumeFormSet(instance=series, prefix="vol")
    title_form = SeriesTitleFormSet(instance=series, prefix="tit")

    if request.POST:

        sub_form = SeriesVolumeFormSet(request.POST, instance=series, prefix="vol")
        form = SeriesForm(request.POST, instance=series, prefix="ser")
        title_form = SeriesTitleFormSet(request.POST, instance=series, prefix="tit")

        if form.is_valid() and sub_form.is_valid() and title_form.is_valid():
            form.save()
            sub_form.save()
            title_form.save()

            return HttpResponseRedirect(series.get_absolute_url())
    return render(request, "directory/series_form.html", {
        "formset" : sub_form,
        "form" : form,
        "titleform" : title_form,
    })

class SeriesUpdate(UpdateView):
    model = Series
    template_name = "directory/form.html"
    fields = ['title', 'author', 'artist', 'tags', 'image', 'synopsis']

class SeriesDelete(DeleteView):
    model = Series
    context_object_name = "object"
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

class VolumeCreate(CreateView):
    model = Volume
    template_name = "directory/form.html"
    fields = ['title', 'number', 'series', 'image']

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
    fields = ['title', 'number', 'series', 'image']

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

class TagCreate(CreateView):
    model = Tags
    template_name = "directory/form.html"
    fields = ['title']

class TagUpdate(UpdateView):
    model = Tags
    template_name = "directory/form.html"
    fields = ['title']

class TagDelete(DeleteView):
    model = Tags
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            series_list = Series.objects.filter(Q(title__icontains=query) | Q(alttitle__title__icontains=query))

            if series_list.count() == 1:
                series = series_list[0]
                return render(request, 'directory/series_detail.html', {'series' : series})
            else:
                return render(request, 'directory/search_form.html', {'series_list': series_list, 'form': form})
    form = SearchForm()
    return render(request, 'directory/search_form.html', {'form': form})

    # Consider adding haystack for more advanced searching (categories and tags)