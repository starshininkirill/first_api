from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Genre, Director, Movie
import json
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def get(request):

    with open('data.json', encoding="UTF-8") as file:
        data = json.load(file)
        id = 0
        for item in data['movies']:
            item['id'] = id
            id += 1
            print(item)
            movie = MovieSerializer(data=item)
            print(movie.is_valid())
            # print(movie.validated_data)
            # obj = Movie(
            #     title=item['title'],
            #     description=item['description'],
            #     year=item['year'],
            #     rating=item['rating'],
            #     genre_id=int(item['genre_id']),
            #     director_id=int(item['director_id']),
            # )
            # obj.save()

    return JsonResponse({'norm': True})


def test(request):
    movie = Movie.objects.first()
    movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)
    print(serializer.data)
    content = JSONRenderer().render(serializer.data)
    # obj = MovieSerializer(data=serializer.data)
    # obj.is_valid()
    # obj.save()
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'DELETE':
        movie.delete()
        return HttpResponse(status=204)
