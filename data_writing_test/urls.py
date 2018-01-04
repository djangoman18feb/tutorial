from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_data_view, name='home_data'),
    ]