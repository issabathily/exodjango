from django.urls import path
from blog import views

urlpatterns = [
    path('blog/',views.index,name='index'),
    path('form/',views.AjouForms,name='Ajouterpost'),
    path('modifier/<int:id>/', views.modifier_article, name='modifier'),
    path('delete/<int:id>/',views.supprimer_article, name='supprimer_article')
]