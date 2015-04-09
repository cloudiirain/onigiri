__author__ = 'jeffrey'

from django import forms
from django.forms.models import inlineformset_factory
from directory.models import Series, Volume, AltTitle

SeriesVolumeFormSet = inlineformset_factory(Series, Volume, fields=('title', 'number'), extra=2)
SeriesTitleFormSet = inlineformset_factory(Series, AltTitle, fields=('title',), extra=3)

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)