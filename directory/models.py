from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=200, default="", unique=True)
    author = models.CharField(max_length=50, default="")
    artist = models.CharField(max_length=50, default="", blank=True)

    def __unicode__(self):
        return self.title

class Volume(models.Model):
    pass

class Chapter(models.Model):
    pass
