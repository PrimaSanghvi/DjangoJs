from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# urlpatterns[

#     url('/home',views.home),
#     url('/details',views.get_details.as_view({ 'get': 'list', 'post': 'create'})),

# ]
urlpatterns = [
    path('',views.home),
    path('details',views.get_details.as_view({'get': 'list','post': 'create'})),
    path('profileupdate/<str:pk>',views.profileupdate),
     path('profiledelete/<str:pk>',views.profiledelete),
]
