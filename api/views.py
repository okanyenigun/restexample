
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from api.models import Movie
from api.serializer import MovieSerializer


# def get_movies(self):
#     movies = list(Movie.objects.all().values())
#     return JsonResponse({
#         'movies': movies
#     })



# @api_view(['GET'])
# def get_movies(request):
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def movie_create(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def movie(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except:
#         return Response({
#             'error':'Movie does not exist',
#         }, status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == "PUT":
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "DELETE":
#         movie.delete()
#         return Response({
#             'delete':True
#         })


class MovieList(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieCreate(APIView):

    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieRecord(APIView):

    def get_movie_by_pk(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except:
            return Response({
                'error':'Movie does not exist'
            },status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        movie = self.get_movie_by_pk(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_movie_by_pk(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = self.get_movie_by_pk(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)