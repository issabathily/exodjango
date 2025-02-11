from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:id>/', post_details, name='post_details'), 
    path('ajout_post', ajout_post, name='ajout_post'),
  
]