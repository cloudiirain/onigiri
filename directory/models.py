from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models
from django.forms import ModelForm

class Series(models.Model):
    author = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="", blank=True)
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=100, default="", unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail-slug', kwargs={'slug': self.slug})

    def series_slug(self):
        return self.slug

    # Should require the save to occur with the title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['author', 'artist']

class Titles(models.Model):
    title = models.CharField(max_length=100, default="")
    series = models.ForeignKey(Series, default="")
    slug = models.SlugField(max_length=100, default="", unique=True)
    default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # For new entries only
        if self.pk is None:
            list = Titles.objects.filter(series=self.series)
            if list is None:
                self.default = True
            if self.default:
                for item in list:
                    item.default = False
                    item.save()
                # Now update the series section
                self.series.title = self.title
                self.series.slug = self.slug
        super(Titles, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class TitleForm(ModelForm):
    pass

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

class VolumeForm(ModelForm):
    pass

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

class ChapterForm(ModelForm):
    pass