from django import forms
from django.forms import ModelForm
from .models import Photo, Album, Comment

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'image',
            'public',
        ]

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'public',
            'cover_image',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]