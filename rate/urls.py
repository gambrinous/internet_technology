from django.conf.urls import patterns, url
from rate import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^underConstruction/$', views.underConstruction, name='underConstruction'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^test/$', views.test, name='test'),
    url(r'^course/$', views.course, name='course'),
)