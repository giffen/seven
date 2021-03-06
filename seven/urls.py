from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		(r'^accounts/', include('allauth.urls')),
		url(r'^$', 'profiles.views.home', name='home'),
		url(r'^about/$', 'profiles.views.about', name='about'),
		url(r'^contact/$', 'contact.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
