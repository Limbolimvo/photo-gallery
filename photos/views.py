from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from .forms import PhotoForm, AlbumForm
from .models import Photo, Album


class HomeView(ListView):
    model = Photo
    template_name = 'main/home.html'


class PhotosView(ListView):
    model = Photo
    template_name = 'main/photos.html'


class AlbumsView(ListView):
    model = Album
    template_name = 'main/albums.html'


class AddPhoto(CreateView):
    model = Photo
    template_name = 'main/add_photo.html'
    form_class = PhotoForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('photos')


class CreateAlbum(CreateView):
    model = Album
    template_name = 'main/create_album.html'
    form_class = AlbumForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return redirect('albums')


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'main/photo_detail.html'


class AlbumDetail(DetailView):
    model = Album
    template_name = 'main/album_detail.html'


class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos')
    template_name = "main/photo_confirm_delete.html"


class AlbumDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos')
    template_name = "main/album_confirm_delete.html"
