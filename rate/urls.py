from django.conf.urls import patterns, url
from rate import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^underConstruction/$', views.underConstruction, name='underConstruction'),
    url(r'^register/$', views.register, name='register'),
    url(r'^test/$', views.test, name='test'),
)