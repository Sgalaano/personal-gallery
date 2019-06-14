from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^$',views.pictures_of_day,name='picturesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_pictures,name = 'pastPictures'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photos/(\d+)',views.photos,name ='photos'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
