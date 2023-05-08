from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('photos', views.PhotosView.as_view(), name='photos'),
    path('albums', views.AlbumsView.as_view(), name='albums'),
    path('/add', views.AddPhoto.as_view(), name='add_photo'),
    path('album/create', views.CreateAlbum.as_view(), name='create_album'),
    path('photo/detail/<int:pk>', views.PhotoDetail.as_view(), name='photo_detail'),
    path('album/detail/<int:pk>', views.AlbumDetail.as_view(), name='album_detail'),
    path('photo/delete/<int:pk>', views.PhotoDelete.as_view(), name='delete_photo'),
    path('album/delete/<int:pk>', views.AlbumDelete.as_view(), name='delete_album'),

]