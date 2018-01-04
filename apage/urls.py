from django.conf.urls import url
from apage import views

urlpatterns = [
#    url(r'^$', views.index, name='home'),
    url(r'^$', views.index, name='index'),
    #/apage/quotes/popular
    #url(r'^quotes/popular/$', views.popular_quotes, name='popular_quotes'),

    #url(r'^quotes/(?P<pk>\d+)/favorite/$', views.favorite, name='favorite'),
    #/apage/author_detail/pk
    #url(r'^author_detail/(?P<pk>\d+)/$', views.detail, name='author_detail'),

    url(r'^(?P<pk>[0-9]+)/$', views.Detailview.as_view(), name='author_detail'),

  ]