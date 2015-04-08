from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="", blank=True)
    slug = models.SlugField(max_length=100, default="", unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail-slug', kwargs={'slug': self.slug})

    def series_slug(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']

class Volume(models.Model):
    title = models.CharField(max_length=100, default="")
    number = models.FloatField(null=True)
    series = models.ForeignKey(Series, null=True)

    def __unicode__(self):
        return str(self.series) + ": " + self.title

    def get_absolute_url(self):
        return reverse('series-detail-slug', kwargs={'slug': self.series.slug})

    def series_slug(self):
        return self.series.slug

    class Meta:
        unique_together = ('series', 'title')
        ordering = ['series', 'number']

class Chapter(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField(null=True)
    volume = models.ForeignKey(Volume, null=True)

    def __unicode__(self):
        return str(self.volume) + " " + self.title

    def get_absolute_url(self):
        return reverse('series-detail-slug', kwargs={'slug': self.volume.series.slug})

    def series_slug(self):
        return self.volume.series.slug

    class Meta:
        unique_together = ('volume', 'title')
        ordering = ['volume', 'number']