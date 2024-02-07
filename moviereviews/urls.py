"""
URL configuration for moviereviews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from movie import views as movieViews

urlpatterns = [
    # visual admin interface povided for developers within the app to manage the Django project.
    path('admin/', admin.site.urls),
    # routing to movie app's view file home function, creating a default page
    path('', movieViews.home, name='home'),
    # routing to movie app's view file about function, creating an about page
    path('about/', movieViews.about, name='about'),
    # add routing to 2nd app: news. 
    # instead of creating specific paths to each app's view.py, we will make things more structured by creating a urls.py file in each app and use the include function to forward any 'news/' requests to news app's url.py
    path('news/', include('news.urls')),
    # creating a url.py file in movie folder
    path('movie/', include('movie.urls')),
    # creating a url.py file in accounts folder
    path('accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)