from django.urls import path
from . import views

urlpatterns = [
 
     path("", views.index),
     path("useAI", views.useAI),
     path("submit-request", views.submit_request),
     path("submit-result", views.submit_request),
   
]
