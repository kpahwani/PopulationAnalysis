from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^index/$', TemplateView.as_view(template_name='user/home.html')),
    url(r'^display/$', TemplateView.as_view(template_name='user/display.html')),
    url(r'^list_all/$', views.UserList.as_view(), name='list_all'),
    url(r'^gender_count/$', views.gender_count, name='gender_count'),
    url(r'^relationship_count/$', views.relationship_count, name='relationship_count'),
    url(r'^search/gender=(?P<gender>\w+)/race=(?P<race>\w+)/rel=(?P<relation>\w+)/$', views.search, name='search'),
    url(r'^selector_list/$', views.get_selector_list, name='selector_list'),
]