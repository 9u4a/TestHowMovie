import requests
from django.conf import settings
from API.GetData.MovieVideo import MovieVideo
from API.GetData.Recommendations import Recommendations


def SearchDetail(request):

    url = 'https://api.themoviedb.org/3/movie/'
    api_key = '?api_key=' + getattr(settings, 'API_KEY', None)[0]
    language = '&language=ko-KR'

    movie_id = request.GET.get('movie_id')
    res = requests.get(url + movie_id + api_key + language)
    if res.status_code == 401:
        raise Exception(401)
    elif res.status_code == 404:
        raise Exception(404)
    data = res.json()

    result = [{
        'adult': data['adult'],
        'original_language': data['original_language'],
        'original_title': data['original_title'],
        'genres': data['genres'],
        'title': data['title'],
        'overview': data['overview'],
        'poster_path': data['poster_path'],
        'backdrop_path': data['backdrop_path'],
        'release_date': data['release_date'],
        'vote_average': data['vote_average'],
        'vote_count': data['vote_count'],
        'status': data['status'],
        'runtime': data['runtime'],
        'tagline': data['tagline'],
        'video': MovieVideo(request, movie_id, 'search'),
        'recommendations': Recommendations(request)
    }]
    response = {
        'detail': result
    }
    return response
