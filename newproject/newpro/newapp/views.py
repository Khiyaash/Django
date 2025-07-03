from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movies = Movies.objects.all()
    #to get the movie name in search bar we are getting the info from request
    movie_name = request.GET.get('movie_name')
    if movie_name != '' and movie_name is not None:
        movies = movies.filter(name__icontains=movie_name)
    paginator = Paginator(movies,3)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request,'newapp/movie_list.html',{'movies':movies})




"""So that's how you can actually go ahead and implement the search functionality in Django.

So the only thing which you need to use is that you need to use a form.

Then in order to access or get the input fields data from the form, you simply need to go ahead and

use the get method from the request and get that particular forms field using the form field name,

which is movie name.

In this case, then you simply get that movie name and you check if that movie name actually matches

up with the name.

And in order to ease up the search a little bit, you use the variable name, double underscore contains.

And the search is going to work in a much more better way."""