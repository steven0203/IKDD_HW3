from django.conf.urls import url

from . import views


app_name='get_data'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

