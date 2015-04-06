__author__ = 'jeffrey'

from django import forms

class SeriesForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    artist = forms.CharField()

#    def createSeries(self):
#        pass

#    def updateSeries(self):
 #       pass