from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Photos

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pictures_of_day(request):
    date = dt.date.today()
    gallery = Photos.todays_pictures
    return render(request, 'all-galls/today-pics.html', {"date": date,"gallery":gallery})

def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Sarturday',"Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_pictures(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pictures_of_day)

    pictures = Photos.days_pictures(date)
    return render(request, 'all_galls/past-pics.html',{"date": date,"pictures":pictures})

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = Photos.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-galls/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galls/search.html',{"message":message})

def photos(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)

    except DoesNotExist:

        raise Http404()
    return render(request,"all-galls/photos.html", {"photo":photo})
