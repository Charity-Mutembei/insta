from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url(r'^$', views.welcome, name = 'welcome'),
    url(r'^post$', views.new_post, name='new-post'),
    url(r'^profile$', views.userProfile, name='profile'),
    url(r'^profile-edit$', views.userProfileEdit, name='profile-edit'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
