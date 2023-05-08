from django.conf import settings
from django.db import models
import PIL
from PIL import Image


class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.country}"

    def save_location(self):
        return self.save()

    class Meta:
        ordering = ["country"]
        verbose_name = 'Location'


class Album(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField("title", max_length=255)
    slug = models.SlugField("slug", max_length=255, unique=True)
    description = models.CharField("description", max_length=255)
    shot_date = models.DateField("shot date", null=True, blank=True)

    def __str__(self):
        return self.title

    def save_category(self):
        return self.save()

    class Meta:
        ordering = ["title"]
        verbose_name = 'Album'


class Photo(models.Model):
    album = models.ManyToManyField(
        Album,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.CASCADE
    )
    title = models.CharField("title", max_length=255)
    photo = models.ImageField("photo", upload_to='images/', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    tags = models.CharField(max_length=64, blank=True, default=list)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.photo.path)
        output_size = (500, 500)
        img.thumbnail(output_size)
        img.save(self.photo.path)

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Photo'