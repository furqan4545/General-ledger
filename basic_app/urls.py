from django.conf.urls import url
from django.urls import path
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('', views.ProductListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name="detail"),
    url(r'^create/$', views.ProductCreateView.as_view(), name="create"),
    url(r'^update/(?P<pk>\d+)/$', views.ProductUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>\d+)/$', views.ProductDeleteView.as_view(), name="delete"),
    path('people/', views.PeopleListView.as_view(), name="people_list"),
    url(r'^people/(?P<pk>\d+)/$', views.PeopleDetailView.as_view(), name="people_detail"),
    url(r'^people/create/$', views.PeopleCreateView.as_view(), name="people_create"),
    url(r'^people/update/(?P<pk>\d+)/$', views.PeopleUpdateView.as_view(), name="people_update"),
    url(r'^people/delete/(?P<pk>\d+)/$', views.PeopleDeleteView.as_view(), name="people_delete"),
    
    
]