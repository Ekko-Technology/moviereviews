from django.shortcuts import render
from .models import News

# Create your views here.
def news(request):
    # order the display of articles by the date attribute within the news class
    newss = News.objects.all().order_by('-date')
    return render(request, "news.html", {'newss': newss})