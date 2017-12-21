from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.





class Image(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    profile_pic = models.ImageField()


    def __unicode__(self):
        return self.first_name or u'' + self.last_name or u'' 







class Album(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    general = models.CharField(max_length=250)
    album_logo = models.ImageField()



    def get_absolute_url(self):
        return reverse('album:detail' , kwargs={'pk':self.id})





    def __unicode__(self):
        return self.artist or u'' + self.title or u''

class Song(models.Model):
    CHOICES = (
    ('ogg', 'Ogg'),
    ('mp3', 'Mp3'),
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    file_type = models.CharField(choices=CHOICES, default='mp3' , max_length=200)
    is_favorite = models.BooleanField(default=False)
    music_file = models.FileField(upload_to = 'media/%Y/%m/%d/') 
















