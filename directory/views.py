from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator


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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SeriesCreate, self).dispatch(*args, **kwargs)

@login_required
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SeriesUpdate, self).dispatch(*args, **kwargs)

class SeriesDelete(DeleteView):
    model = Series
    context_object_name = "object"
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SeriesDelete, self).dispatch(*args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VolumeCreate, self).dispatch(*args, **kwargs)

class VolumeUpdate(UpdateView):
    model = Volume
    template_name = "directory/form.html"
    fields = ['title', 'number', 'series', 'image']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VolumeUpdate, self).dispatch(*args, **kwargs)

class VolumeDelete(DeleteView):
    model = Volume
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VolumeDelete, self).dispatch(*args, **kwargs)

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChapterCreate, self).dispatch(*args, **kwargs)

class ChapterUpdate(UpdateView):
    model = Chapter
    template_name = "directory/form.html"
    fields = ['title', 'number', 'volume']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChapterUpdate, self).dispatch(*args, **kwargs)

class ChapterDelete(DeleteView):
    model = Chapter
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChapterDelete, self).dispatch(*args, **kwargs)

class TagCreate(CreateView):
    model = Tags
    template_name = "directory/form.html"
    fields = ['title']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagCreate, self).dispatch(*args, **kwargs)

class TagUpdate(UpdateView):
    model = Tags
    template_name = "directory/form.html"
    fields = ['title']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagUpdate, self).dispatch(*args, **kwargs)

class TagDelete(DeleteView):
    model = Tags
    template_name = "directory/confirm_delete.html"
    success_url = reverse_lazy('series-list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagDelete, self).dispatch(*args, **kwargs)

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            series_list = Series.objects.filter(Q(title__icontains=query) | Q(alttitle__title__icontains=query))
            refined_list = []
            for series in series_list:
                if not series in refined_list:
                    refined_list.append(series)

            if len(refined_list) == 1:
                series = refined_list[0]
                return render(request, 'directory/series_detail.html', {'series' : series})
            else:
                return render(request, 'directory/search_form.html', {'series_list': refined_list, 'form': form})
    form = SearchForm()
    return render(request, 'directory/search_form.html', {'form': form})

    # Consider adding haystack for more advanced searching (categories and tags)