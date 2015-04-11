__author__ = 'cloudiirain'

from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from directory.models import Series, Volume, AltTitle, Tags

SeriesVolumeFormSet = inlineformset_factory(Series, Volume, fields=('title', 'number'), extra=2)
SeriesTitleFormSet = inlineformset_factory(Series, AltTitle, fields=('title',), extra=3)

class SearchForm(forms.Form):
    query = forms.CharField(label='',
                            max_length=100,
                            widget=forms.TextInput(
                                attrs={'class' : 'form-control', 'placeholder' : 'search for light novel fan translations',}
                            ))

class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['title']

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'author', 'artist', 'tags', 'image', 'synopsis']


class TitleForm(ModelForm):
    class Meta:
        model = AltTitle
        fields = ['title']

class VolumeForm(ModelForm):
    pass

class ChapterForm(ModelForm):
    pass