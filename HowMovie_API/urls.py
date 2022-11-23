"""HowMovie_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions

from API.Views.CommentView import CommentView
from API.Views.GenreView import GenreView
from API.Views.MovieDetailView import MovieDetailView
from API.Views.MainView import MainView
from API.Views.NowPlayingView import NowPlayingView
from API.Views.SearchDetailView import SearchDetailView
from API.Views.SearchView import SearchView
from API.Views.TopRatedView import TopRatedView
from API.Views.TrendingView import TrendingView
from API.Views.PopularView import PopularView
from API.Views.UpComingView import UpComingView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from HowMovie_API import settings

schema_view = get_schema_view(
   openapi.Info(
      title="HowMovie API",
      default_version='ver1.0',
      description="HowMovie Test API 작성자 : 이준성",
      terms_of_service="",
      contact=openapi.Contact(name="이준성", email="99junsung@gmail.com"),
      license=openapi.License(name="HM License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trend', TrendingView.as_view()),
    path('popular', PopularView.as_view()),
    path('upcoming', UpComingView.as_view()),
    path('nowplaying', NowPlayingView.as_view()),
    path('toprated', TopRatedView.as_view()),
    path('main', MainView.as_view()),
    path('moviedetails', MovieDetailView.as_view()),
    path('search', SearchView.as_view()),
    path('searchdetails', SearchDetailView.as_view()),
    path('genre', GenreView.as_view()),
    path('comments', CommentView.as_view()),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ]
