from django.urls import path
from . import views

urlpatterns = [
 
     path("", views.index),
     path("get", views.getdata),
     path("login", views.postdata),
     path("submit-request", views.submit_request),
     path("submit-result", views.submit_result),
     path("fetch-request", views.fetchRequest),
     path("get-result/<int:id>/", views.getresult_id ,name="get-result"),
      
 
]
