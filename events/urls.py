from django.urls import path
from . import views

urlpatterns = [
    path('event_list/', views.event_list, name='event_list'),
    path('add_event/', views.add_event, name='add_event'),
     path('index/', views.index, name='index'),
     path('index/AllEvents/',views.allevents,name='allevents'),
     path('index/eventsdata/',views.eventsdata,name='eventsdata' )
]
