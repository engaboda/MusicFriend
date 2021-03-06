from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Album , Song 
from django.template import loader
from django.db.models import Q
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .forms import SignUpForm , EditProfileForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.core import serializers
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.core import serializers

import json
from .forms import ImageUpload , UploadMusic

# Create your views here.

#class IndexView(generic.ListView):
 #   template_name = 'album/home.html'
  #  def get_queryset(self):
   #     return Album.objects.all()


def index(request):
    album = Album.objects.all()


    context = {
        "object_list":album,
       
    }
    return render(request , 'album/home.html' , context)





###################################### create album using create view
class CreateAlbum(CreateView):
    model = Album

    fields = [
        'title',
        'artist',
        'general',
        'album_logo',
        'user',
    ]

#########################################################create view






def creatView(request):
    if request.method=='POST':
        form = ImageUpload(request.POST , request.FILES)
        user =request.session.get('user')
        data = json.loads(user)
        album = Album(title=request.POST.get('title') , artist = request.POST.get('artist') , general=request.POST.get('general') , album_logo=request.FILES['image'] , user_id=data[0]['pk'])
        album.save()
        return redirect('/album')
    else:
        form = ImageUpload()
        return render(request,'album/create_album.html' , {'form':form})

   




##########################################################details










def detail(request , pk):
    current_album = Album.objects.filter(pk=pk)
    song = Song.objects.filter(album_id=pk)
    context = {
        "albums":current_album,
        "songs":song
    }

    return render(request , 'album/detail.html' , context)










############################################################favorite
def favorite(request):
    
    favorite = request.GET.get('favorite')
    bad = request.GET.get('bad')

    album_id = request.GET.get('id')

    current_album = Album.objects.filter(pk=album_id)

    album = Album.objects.get(id=album_id)

    id_song = request.GET.get('song_id')
    template = loader.get_template('album/detail.html')

    songs = album.song_set.all()  


    if request.method=='GET':
        if favorite=='on':
            context = {
                "albums":current_album,
                "songs":songs
            }
            song = Song.objects.get(id=id_song)
            song.is_favorite=True
            song.save()
            return HttpResponse(template.render(context,request))

        elif bad=='on':
            context = {
                    "albums":current_album,
                    "songs":songs
                }           
            song = Song.objects.get(id=id_song)
            song.is_favorite=False
            song.save()
            return HttpResponse(template.render(context,request))

        elif album_id != None or id_song !=None:
            context = {
                        "albums":current_album,
                        "songs":songs
                    }      
            return HttpResponse(template.render(context,request))




##################################################delete album
def deletealbum(request , pk):
    if request.method == 'POST':
        album  = Album.objects.get(pk=pk)
        album.delete()
        return redirect('album:index')


###################################################search in all album in all fields


def searchview(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        album = Album.objects.filter(Q(title__contains=query) | Q(artist__contains=query)  |  Q(general__contains=query) )
        context = {
            "object_list":album
            }
        return render(request,'album/home.html' , context)








######################################################signup 




def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)

        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            template = loader.get_template('album/home.html')
            user = User.objects.filter(username=username)
            data = serializers.serialize('json' , list(user) , fields=('username','first_name' , 'last_name' , 'email' ))
            request.session['user']
            return redirect('/album')
               
        else:
            return render(request,'album/signup.html' , {'form':form })                       
    else:
        form = SignUpForm()
        return render(request,'album/signup.html' , {'form':form})





##############################sign in using session





def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        print user
        user_login = User.objects.filter(username=user)

        request.session['user']=serializers.serialize('json' ,  user_login , fields=('username' , 'first_name' , 'last_name' , 'email'  ,'password' ))

        login(request,user)
        return redirect('/album')

    else:
        return render(request , 'album/signin.html' , {})







###############################################profile





def signout(request,pk):
    if request.method=='GET':
        user = User.objects.get(pk=pk)
        logout(request)
        print request.user
        return redirect('/album/signin')
    else:
        pass



###########################################################
def profile(request):
    if request.method=='POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 


        return redirect('/album')
    else:
        return render(request,'album/profile.html' , {})



#########################################




#def edit_profile(request):
 #   if request.method == 'POST':
  #      username = request.POST['username']
  #      first_name = request.POST['first_name']
  #      last_name = request.POST['last_name']
   #     email = request.POST['email']
   #     password = request.POST['password']
  #      user = 
  #      return redirect('/album/profile')


#    else:
 #       return render(request,'album/edit_profile.html' , {'form':form})

















#def reqister(request):
 #   if request.method=='POST':
  #          username = request.POST['username']
   #         first_name = request.POST['first_name']
    #        last_name = request.POST['last_name']
     #       email = request.POST['email']
      #      password = request.POST['password']
       #     user = User.objects.create_user(username,first_name,last_name,email,password)
        #    user.save()
         #   return redirect('/album')
                      



####################################### add song 

def hundel_uploaded_file(f):
    with open('media/f', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)



def add_song(request,pk):
    if request.method=='POST':
        form = UploadMusic(request.POST , request.FILES )
        if form.is_valid():
            song = Song.objects.create(user=request.user,album=Album.objects.get(id=pk), title=request.POST.get('title'), file_type=request.POST.get('file_type') , music_file= request.FILES['music_file'])
            song.save()
            return redirect('/album')
    else:
        form = UploadMusic()
        return render(request , 'album/add_song.html' , {'form':form , 'albums':Album.objects.filter(id=pk)})
        	
        	
	
			
			
			
			
			

			
			
			
			
			
			
			








