from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models


class Tags(models.Model):
    title = models.CharField(max_length=50, default="")
    slug = models.SlugField(max_length=50, default="", unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-list')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tags, self).save(*args, **kwargs)


class Series(models.Model):
    author = models.CharField(max_length=50, default="", verbose_name="Series Author")
    artist = models.CharField(max_length=50, default="", blank=True, verbose_name="Series Illustrator")
    title = models.CharField(max_length=100, default="", verbose_name="Series Title")
    slug = models.SlugField(max_length=100, default="", unique=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags, blank=True)
    image = models.URLField(blank=True, null=True, verbose_name="Image URL")
    synopsis = models.TextField(blank=True, default="")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series-detail-slug', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Series, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']


class AltTitle(models.Model):
    title = models.CharField(max_length=100, default="")
    series = models.ForeignKey(Series, default="")
    slug = models.SlugField(max_length=100, default="", unique=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(AltTitle, self).save(*args, **kwargs)


class Volume(models.Model):
    title = models.CharField(max_length=100, default="")
    number = models.FloatField(null=True)
    series = models.ForeignKey(Series, null=True)
    image = models.URLField(blank=True)
    slug = models.SlugField(max_length=100, default="")

    def __unicode__(self):
        return str(self.series) + ": " + self.title

    def get_absolute_url(self):
        return reverse('volume-detail-slug', kwargs={'series': self.series.slug, 'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Volume, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('series', 'slug')
        ordering = ['series', 'number']


class Chapter(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField(null=True)
    volume = models.ForeignKey(Volume, null=True)
    translator = models.CharField(max_length=50, default="")
    url = models.URLField(null=True, default="#")


    def __unicode__(self):
        return str(self.volume) + " " + self.title

    def get_absolute_url(self):
        return reverse('volume-detail-slug', kwargs={'series': self.volume.series.slug, 'slug': self.volume.slug})

    class Meta:
        ordering = ['volume', 'number']
