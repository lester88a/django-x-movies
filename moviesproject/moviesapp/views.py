from django.shortcuts import render
from moviesapp.models import Genre, Movie
from moviesapp.forms import UserForm, UserProfileInfoForm, NewMovieForm
#pagenation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):

    # genres = Genre.objects.order_by('name')
    # moveis = Movie.objects.order_by('year')
    #
    # data_dict = {'genres':genres,'moveis':moveis}
    #return render(request,'moviesapp/index.html',context=data_dict)
    return render(request,'moviesapp/index.html')

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'moviesapp/registration.html',
                            {'user_form':user_form,
                             'profile_form': profile_form,
                             'registered':registered})
@login_required(login_url='/login/')
def add_movie_view(request):

    if request.method == 'POST':
        add_movie_form = NewMovieForm(data=request.POST)

        if add_movie_form.is_valid():
            movie = add_movie_form.save(commit=False)


            movie.save()
        else:
            print(add_movie_form.errors)

    else:
        add_movie_form = NewMovieForm()

    return render(request,'moviesapp/add.html',
                            {'add_movie_form':add_movie_form})
#@login_required(login_url='/login/')
def movies(request):
    movies_list = Movie.objects.all()
    genres = Genre.objects.order_by('name')

    paginator = Paginator(movies_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)

    data_dict = {'movies':movies,'genres':genres}

    return render(request,'moviesapp/movies.html',context=data_dict)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('someone tried to login and failed.')
            print('Username: {0} and password {1}'.format(username,password))
            return HttpResponse('invalid login details supplied.')

    return render(request,'moviesapp/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
