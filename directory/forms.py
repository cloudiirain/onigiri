__author__ = 'jeffrey'

from django import forms
from django.forms.models import inlineformset_factory
from directory.models import Series, Volume, AltTitle

SeriesVolumeFormSet = inlineformset_factory(Series, Volume, fields=('title', 'number'), extra=2)
SeriesTitleFormSet = inlineformset_factory(Series, AltTitle, fields=('title',), extra=3)

class SearchForm(forms.Form):
    query = forms.CharField(label='',
                            max_length=100,
                            widget=forms.TextInput(
                                attrs={'class' : 'form-control', 'placeholder' : 'Search',}
                            ))