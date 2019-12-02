from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload_hood, name='upload'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^accounts/update/', views.edit, name='update_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^search_biz/', views.search_category, name='search_category'),
    url(r'^hood/(?P<hood_id>\d+)', views.hood, name='hood'),
    url(r'^join(?P<hood_id>\d+)', views.join, name='join'),
    url(r'^leave/(?P<hood_id>\d+)', views.leave, name='leave'),
    url(r'^upload_business/', views.upload_business, name='upload_business'),
    url(r'^post/', views.add_post, name='post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
