from django.urls import path
from blog import views

urlpatterns = [
    path('blog/',views.index,name='index'),
    path('form/',views.Ajouterpost,name='Ajouterpost'),
]