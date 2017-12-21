from django.contrib import admin
from .models import Album , Song  , Image
# Register your models here.



class SongAdminModel(admin.ModelAdmin):
    list_display = ['album' , 'title' , 'file_type' , 'is_favorite']
    class meta:
        model = Song

class AlbumAdminModel(admin.ModelAdmin):
    list_display = ['user' , 'title' , 'artist' , 'general' , 'album_logo' , 'id']
    class meta:
        model = Album

class ImageAdminModel(admin.ModelAdmin):
	list_display =['profile_pic' , 'user' ]
	class meta:
		model=Image

admin.site.register(Album , AlbumAdminModel)
admin.site.register(Song , SongAdminModel)
admin.site.register(Image,ImageAdminModel)