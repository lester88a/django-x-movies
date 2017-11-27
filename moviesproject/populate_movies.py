import pandas as pd

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesproject.settings')

import django
django.setup()

import csv
from moviesapp.models import Movie, Genre
from django.utils import timezone
#movies = pd.read_csv('/home/lester/Downloads/newmovies.csv')

genres = ['Drama', 'Action', 'Crime', 'Adventure', 'Comedy', 'Sci-Fi',
       'Mystery', 'Biography', 'Horror', 'Animation', 'Thriller', 'Family',
       'Documentary', 'Romance', 'Short', 'Reality-TV', 'Western',
       'Fantasy', 'News', 'History', 'Game-Show', 'Music', 'Musical',
       'Talk-Show', 'Sport', 'War']

#reader = csv.reader('/home/lester/Downloads/mov.csv')

def populate():
    for r in genres:
        genre = Genre.objects.get_or_create(name=r)



    # for row in reader:
    #
    #     print(len(row[1]))
    #
    #     mygenres = []
    #     for g in row[4]:
    #         mygenres.append(g)
    #     print(mygenres)
    #     movie = Movie.objects.get_or_create(title = row[1],
    #                                         year = row[2],
    #                                         rate = row[3],
    #                                         genres = mygenres,
    #                                         votes = row[5],
    #                                         runtime = row[6],
    #                                         desc = row[7],
    #                                         dateadded = timezone.now
    #                                         )


    import csv
    with open('/home/lester/Downloads/newmovies.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        mygenres = []
        for row in reader:
            #print(row['title'], row['rYear'])
            mygenres = Genre.objects.get_or_create(name=row['genre'])
            #print('-----------------------------'+mygenres[0].name)
            movie = Movie.objects.create(title = row['title'],
                                                    year = int(row['rYear']),
                                                    rate = float(row['rate']),
                                                    #genres = mygenres[0],
                                                    votes = int(float(row['votes'])),
                                                    runtime = row['rRuntime'],
                                                    desc =row['desc'],
                                                    #dateadded = timezone.now
                                                    )
            movie.genres.add(mygenres[0])


if __name__ == '__main__':
    print('populating script!')
    populate()
    print('populating compalete!')
