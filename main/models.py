from django.db import models


# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50, unique=True, default='도시이름')
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name
