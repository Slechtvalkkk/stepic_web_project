from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/', 'qa.views.test1'),
    url(r'^login/', ''),
    url(r'^signup/', ''),
    url(r'^questions/<qnum>/', 'qa.views.test'),
    url(r'^ask/', ''),
    url(r'^popular/', ''),
    url(r'^new/', '')
)
