from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    #url(r'^', include("qa.urls"))
    url(r'^$', views.test),
    url(r'^login/.*$', views.test),
    url(r'^signup/.*$', views.test),
    url(r'^questions/\d+/$', views.test),
    url(r'^ask/.*$', views.test),
    url(r'^popular/.*$', views.test),
    url(r'^new/.*$', views.test)
]