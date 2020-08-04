from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.views import View
from users.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_albums') 
    return render(request, 'core/home.html')

@login_required
def list_albums(request):
    albums = request.user.albums.all()
    return render(request, 'core/list_albums.html', {'albums': albums})


@login_required
def list_photos(request):
    photos = request.user.photos.all()
    form = PhotoForm()
    return render(request, 'core/list_photos.html', {'photos': photos, 'form': form})


@login_required
def show_photo(request, pk):
    photo = get_object_or_404(request.user.photos, pk=pk)
    form = PhotoForm()
    photos = photo.photos.order_by('date_uploaded')
    # user_favorite = request.user.is_starred_photo(photo)
    return render(request, 'core/show_photo.html', {'photo': photo, 'form': form, 'photos': photos, 'pk':pk})


@login_required
def show_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    form = AlbumForm()
    photos = album.photos.order_by('date_uploaded')
    # user_favorite = request.user.is_starred_album(album)
    return render(request, 'core/show_album.html', {'album': album, 'pk': pk, 'form': form, 'photos': photos})


def add_photo(request):
    if request.method == 'GET':
        form = PhotoForm()
    else:
        form = PhotoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.instance
            photo.user = request.user
            photo.save()
            return redirect(to='list_photos')

    return render(request, 'core/add_photo.html', {'form': form})    


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            album = form.instance
            album.user = request.user
            album.save()
            return redirect(to='list_albums')

    return render(request, 'core/add_album.html', {'form': form})


@login_required
def add_photo_to_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = PhotoForm()
    else:
        form = PhotoForm(data=request.POST)
        if form.is_valid():
            photo = form.instance
            photo.owner = request.user
            photo.album = album
            photo.save()
            return redirect(to='show_album', pk=pk)
    return render(request, 'core/add_photo_to_album.html', {'form': form, 'album': album})


@login_required
def edit_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect(to='list_albums')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'core/edit_album.html', {'form': form, 'album': album})


@login_required
def delete_album(request, pk):
    album = get_object_or_404(request.user.albums, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, 'core/delete_album.html', {'album': album})


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(request.user.photos, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect(to='list_photos')

    return render(request, 'core/delete_photo.html', {'photo': photo})


@login_required
@csrf_exempt
@require_POST
def toggle_starred_album(request, pk):    
    album = get_object_or_404(request.user.albums, pk=pk)
    if album in request.user.starred_album.all():
        request.user.starred_album.remove(album)
        return JsonResponse({"starred": False})
    else:
        request.user.starred_album.add(album)
        return JsonResponse({"starred": True})


@login_required
@csrf_exempt
@require_POST
def toggle_starred_photo(request, pk):    
    photo = get_object_or_404(request.user.photos, pk=pk)
    if photo in request.user.starred_photo.all():
        request.user.starred_photo.remove(photo)
        return JsonResponse({"starred": False})
    else:
        request.user.starred_photo.add(photo)
        return JsonResponse({"starred": True})


def profile(request):
    albums = request.user.albums.all()
    return render(request, 'core/list_albums.html', {'albums': albums})

def search_photos(request):
    pass


