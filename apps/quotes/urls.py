from django.conf.urls import url
from . import views        # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$',views.add),
    url(r'^remove$',views.remove),
    url(r'^postquote$',views.postquote)
]