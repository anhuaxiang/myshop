from django.conf.urls import url
from . import views


app_name = 'order'


urlpatterns = [
    url(r'^created/$', views.order_create, name='order_create'),
]