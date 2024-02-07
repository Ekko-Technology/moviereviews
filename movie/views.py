from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, Review
from .forms import ReviewForm
# adds authorization to access certain features
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    movie_searched = request.GET.get("movieName")
    if movie_searched:
        # queryset operation used to filter out objects, in this case the title field, in the Movie model
        # icontains field lookup modifier that performs a case-insensitive containment test.
        movies = Movie.objects.filter(title__icontains=movie_searched)
    else:
        movies = Movie.objects.all()

    return render(request, 'homepage.html', {'movie_searched': movie_searched, 'movies': movies})


def about(request):
    return HttpResponse('<h1> Welcome to the About page </h1>')

def signup(request):
    username = request.GET.get("username")
    server = request.GET.get("server")
    return render(request, "signup.html", {"username": username, "server":server})


def detail(request, movie_id):
    # django's databases come with a default auto-incremented primary key(pk) for each field thus we are passing in the movie's ID from the admin interface and finding for match with the movie model. if no match, django raises a http404 exception
    movie = get_object_or_404(Movie, pk=movie_id)
    # filtering and retrieving movie reviews from movie database
    reviews = Review.objects.filter(movie = movie)
    return render(request, "details.html", {'movie':movie, 'reviews' : reviews})


@login_required
def createreview(request, movie_id):
    # obtaining movie object from database
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "GET":
        return render(request, 'createreview.html', {'form': ReviewForm(), 'movie': movie})
    
    else:
        try:
            # retrieve submitted form after request
            form = ReviewForm(request.POST) 
            # create and save the new review object  from the form's value but do not commit into database yet
            newReview = form.save(commit=False)
            # reason to not commit just yet is to associate new review with user and movie id
            newReview.user = request.user
            newReview.movie = movie
            # now we can commit the transfer into the db
            newReview.save()
            return redirect('detail', newReview.movie.id)
        
        except ValueError:
            return render(request, 'createreview.html', {'form': ReviewForm(), 'error': 'bad data passed in'})


@login_required     
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == "GET":
        # instance=review helps populate the html template with its original contents for users to edit the existing infos.
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', {'review': review, 'form': form})
    
    else: 
        try:
            # sends the content within the form and updates the database accordingly
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movie.id)

        except ValueError:
            return render(request, 'updatereview.html', {'review': review, 'form': form, 'error': 'Bad data in form'})


@login_required  
def deletereview(request, review_id):
    # last parameter passes in logged-in usewr to ensure other users can't access the review
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    # delete column from database
    review.delete()
    return redirect('detail', review.movie.id)