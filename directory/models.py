from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=200, default="", unique=True)
    author = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="", blank=True)

    def __unicode__(self):
        return self.title

class Volume(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField()
    series = models.ForeignKey(Series)

    def __unicode__(self):
        return self.series + ": " + self.title

    class Meta:
        unique_together = ('series', 'title',)

class Chapter(models.Model):
    title = models.CharField(max_length=200, default="")
    number = models.FloatField()
    volume = models.ForeignKey(Volume)

    def __unicode__(self):
        return self.volume + " " + self.title

    class Meta:
        unique_together = ('volume', 'title',)