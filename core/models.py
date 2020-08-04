from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from users.models import User
from django.conf import settings


class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length = 50)
    public = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)



class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='photos')
    title = models.CharField(max_length=255)
    albums = models.ManyToManyField(Album, related_name='photos', blank=True)
    public = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    thumbnail_image = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    date_uploaded = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)


