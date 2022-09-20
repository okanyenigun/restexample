from django.urls import path
# from api.views import get_movies, movie_create, movie, MovieList
from api.views import MovieList, MovieCreate, MovieRecord
# urlpatterns = [
#     path('', movie_create),
#     path('list/', get_movies),
#     path('<int:pk>', movie)
# ]

urlpatterns = [
    path('',MovieCreate.as_view()),
    path('list/', MovieList.as_view()),
    path('<int:pk>',MovieRecord.as_view())
]
