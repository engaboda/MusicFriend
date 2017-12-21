from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Album , Song


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=250 , help_text="enter your first name")
    password1 = forms.CharField(max_length=250 , help_text="strong password" , widget=forms.PasswordInput)
    last_name = forms.CharField(max_length=250 , help_text="enter your last name")
    email = forms.EmailField(max_length=250 , help_text="requird valid email address")
    username = forms.CharField(max_length=250 , help_text="username ")

    class meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )
    def save(self,commit=True):
    	user = super(SignUpForm , self).save(commit=False)
    	user.first_name = self.cleaned_data['first_name']
    	user.last_name = self.cleaned_data['last_name']
    	user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
    	if commit==True:
    		user.save()

    	return user




class EditProfileForm(UserChangeForm):


	class meta:
	    model = User
	    fields = (
	         'first_name', 'last_name', 'email' , 'password',
	    )



class ImageUpload(forms.Form):
    image = forms.ImageField()
    class meta:
        model=Album
        fields = (
            'album_logo',
            )
            
            
            
            
class UploadMusic(forms.Form):
	music_file = forms.FileField()
	
	class meta:
		model = Song
		fields = (
			'music_file',
			)
			
			
			
			
			
			
			
			
			
			
			
			
