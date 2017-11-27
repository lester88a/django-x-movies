from django.contrib import admin
from moviesapp.models import UserProfileInfo, Genre, Movie
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Genre)
admin.site.register(Movie)
