__author__ = 'jeffrey'

from django import forms
from django.forms.models import inlineformset_factory
from directory.models import Series, Volume

class SeriesForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    artist = forms.CharField()


SeriesVolumeFormSet = inlineformset_factory(Series, Volume, fields=('title', 'number'), extra=2)