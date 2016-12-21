from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^(?P<id>\d+)/message$', views.message),
    url(r'^logout', views.logout),
    url(r'^(?P<id>\d+)/comments', views.comments),
    url(r'^(?P<id>\d+)/user/show', views.show),
    url(r'^(?P<id>\d+)/delete_comment', views.delete_comment),
   	url(r'^(?P<id>\d+)/delete_message', views.delete_message),
    url(r'^signin', views.signin),
    url(r'^add_user', views.add_user)


    


]
