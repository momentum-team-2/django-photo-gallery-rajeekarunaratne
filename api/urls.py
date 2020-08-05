from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import PhotoViewSet, UserViewSet, api_root, AlbumViewSet
from rest_framework import renderers


album_list = AlbumViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
album_detail = AlbumViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
photo_list = PhotoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
photo_detail = PhotoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('albums/', album_list, name='album-list'),
    path('albums/<int:pk>/', album_detail, name='album-detail'),
    path('photos/', photo_list, name='photo-list'),
    path('photos/<int:pk>/', photo_detail, name='photo-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)