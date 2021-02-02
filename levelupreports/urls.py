from django.urls import path
from .views import usergame_list, event_host_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/attendees', event_host_list)
]
