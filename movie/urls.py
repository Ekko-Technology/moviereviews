from django.urls import path
from . import views

urlpatterns = [
    # the additional parameter (name='<page>') is used for additional href coming from other pages' GET request to app views 
    path('signup/', views.signup, name='signup'),
    # creating a unique movie page for each movie
    # when user clicks on a movie, it will reflect the movie's index in the url (eg. "localhost:8000/movie/4) where the value 4 will be associated to the movie_id variabl in 'int:movie_id'.
    path('<int:movie_id>', views.detail, name='detail'),
    # path to direct users to a create reviews page
    path('<int:movie_id>/create', views.createreview,name="create_review"),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', views.deletereview, name='deletereview'),
]