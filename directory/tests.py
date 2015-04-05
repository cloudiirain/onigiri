from django.test import TestCase

from directory.models import Series, Volume, Chapter

class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

class SeriesTest(TestCase):
    def test_create_series(self):
        # Create Series
        series = Series()

        # Set the attributes
        series.title = 'Ore no Imouto ga Konna ni Kawaii Wake ga Nai'
        series.author = 'Tsukasa Fushimi'
        series.artist = 'Hiro Kanzaki'

        # Save it
        series.save()

        # Check if we can find it
        all_series = Series.objects.all()
        self.assertEquals(len(all_series), 1)
        only_series = all_series[0]
        self.assertEquals(only_series, series)

        # Check attributes
        self.assertEquals(only_series.title, 'Ore no Imouto ga Konna ni Kawaii Wake ga Nai')
        self.assertEquals(only_series.author, 'Tsukasa Fushimi')
        self.assertEquals(only_series.artist, 'Hiro Kanzaki')