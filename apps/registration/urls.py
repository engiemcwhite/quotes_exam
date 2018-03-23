from django.conf.urls import url
from . import views        # This line is new!

urlpatterns = [
    url(r'^main$', views.index),
    url(r'^registration$',views.registration),
    url(r'^login$',views.login),
    url(r'^users/(?P<number>\d+)$',views.userpage),
    url(r'^logout$',views.logout)
   
]
