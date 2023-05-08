from django import forms

from .models import Location, Album, Photo
from django.forms import ModelForm, TextInput, DateInput


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ["city", "country"]
        widgets = {
            "city": TextInput(attrs={
                'class': 'form-control'
            }),
            "country": TextInput(attrs={
                'class': 'form-control'
            }),
        }


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description", "shot_date"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control'
            }),
            "description": TextInput(attrs={
                'class': 'form-control'
            }),
            "shot_date": DateInput(attrs={
                'class': 'form-control',
            }),
        }


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ["album", "location", "title", "photo", "tags"]
        widgets = {
            "album": TextInput(attrs={
                'class': 'form-control'
            }),
            "location": TextInput(attrs={
                'class': 'form-control'
            }),
            "title": TextInput(attrs={
                'class': 'form-control'
            }),
            "tags": TextInput(attrs={
                'class': 'form-control'
            }),
        }
