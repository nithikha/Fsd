from django.urls import path 
from myapp import views 
urlpatterns = [ 
path("current_datetime/", views.current_datetime, name="current_datetime"), 
path("date_time_offset/", views.date_time_offset, name="date_time_offset"),
]
