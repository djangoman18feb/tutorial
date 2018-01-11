from django.conf.urls import url
from apage import views

urlpatterns = [
#    url(r'^$', views.index, name='home'),
    url(r'^$', views.index, name='index'),
    #/quotes/popular
    #url(r'^popular/$', views.popular_quotes, name='popular_quotes'),

    #url(r'^(?P<pk>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),

    #url(r'^author_detail/(?P<pk>\d+)/$', views.detail, name='author_detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.Detailview.as_view(), name='author_detail'),

  ]

#Not working code giving reverse not found error
# #/quote/quote_id/favorite/
# url(r'^(?P<quote_id>[0-9]+)/favorite/$', views.favorite, name='favorite_quote'),
#
