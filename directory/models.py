from django.core.urlresolvers import reverse
from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=200, default="", unique=True)
    author = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="", blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['title']

class Volume(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField()
    series = models.ForeignKey(Series)

    def __unicode__(self):
        return self.series + ": " + self.title

    class Meta:
        unique_together = ('series', 'title')
        ordering = ['series', 'number']

class Chapter(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField()
    volume = models.ForeignKey(Volume)

    def __unicode__(self):
        return self.volume + " " + self.title

    class Meta:
        unique_together = ('volume', 'title')
        ordering = ['volume', 'number']