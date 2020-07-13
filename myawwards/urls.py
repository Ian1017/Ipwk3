from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
        url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^api/', include(router.urls)),
    url(r'^(?P<username>\w+)/profile', views.user_profile, name='userprofile'),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/(?P<username>\w+)/settings', views.edit_profile, name='edit'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^project/(?P<id>\d+)',views.project, name='project'),
    url(r'^search/$', views.search_project, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    