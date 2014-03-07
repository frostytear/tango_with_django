__author__ = 'leif'

from django.conf.urls import patterns, url
from showcase import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^cats/(?P<catid>\w+)/$', views.category, name='cat'),
        url(r'^team/(?P<teamid>\w+)/$', views.team, name='team'),
        url(r'^demo/show/(?P<demoid>\w+)/$', views.demo, name='demo'),
        url(r'^demo/rate/(?P<demoid>\w+)/$', views.demo_rate, name='rate_demo'),
        url(r'^demo/add/$', views.demo_add, name='add_demo'),
        url(r'^demo/$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^register/team/$', views.register_team, name='register_team'),
        url(r'^register/rater/$', views.register_rater, name='register_rater'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
)
