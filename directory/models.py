from django.db import models


class Country(models.Model):
    """Модель Страны."""

    name = models.CharField('Страна', max_length=20, blank=True)
    ofsh = models.BooleanField('Офшора')

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.name)

    class Meta:
        """Метакласс модели."""
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Region(models.Model):
    """Регион."""

    name = models.CharField('Регион', max_length=20, blank=True)
    country = models.ForeignKey('Country', verbose_name='Страна', on_delete=models.CASCADE)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.name)

    class Meta:
        """Метакласс модели."""

        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    """Город."""

    name = models.CharField('Город', max_length=20, blank=True)
    region = models.ForeignKey('Region', verbose_name=20, on_delete=models.CASCADE)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.name)

    class Meta:
        """Метакласс модели."""

        verbose_name = 'Город'
        verbose_name_plural = 'Города'