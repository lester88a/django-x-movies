from django.conf.urls import url
from moviesapp import views

# Template Tagging

app_name = 'moviesapp'

urlpatterns = [
    url(r'^movies/$',views.movies,name='movies'),
    #url(r'^register/$',views.register,name='register'),
    #url(r'^login/$',views.login_view,name='login'),
    url(r'^add/$',views.add_movie_view,name='add'),

]
