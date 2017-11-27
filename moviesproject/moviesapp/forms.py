from django import forms
from django.contrib.auth.models import User
from moviesapp.models import UserProfileInfo, Genre, Movie

# class MovieForm(forms.Form):
#     title = models.CharField(max_length=128,unique=True)
#     year =  models.IntegerField(max_length=4)
#     runtime = models.IntegerField(max_length=4)
#     #genres = models.ForeignKey(Genre)
#     votes = models.IntegerField()
#     rate = models.FloatField(max_length=4)
#     desc = models.CharField(widget=forms.Textarea)
#     dateadded = models.DateField(default=timezone.now)

class NewMovieForm(forms.ModelForm):
    class Meta():
        model = Movie
        fields = ('title','year', 'runtime', 'genres','votes', 'rate', 'desc','dateadded')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','wechat', 'qq', 'mobile','gender')
