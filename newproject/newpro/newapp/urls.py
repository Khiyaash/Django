from .import views
from django.urls import include, path

app_name= 'newapp'
urlpatterns = [
    path('movies/',views.movie_list,name='movie_list')
]
