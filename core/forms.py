from django import forms
from django.forms import ModelForm
from .models import Photo, Album

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'image',
            'owner',
            'public',   
            'albums',         
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'public',
            'owner',
        ]