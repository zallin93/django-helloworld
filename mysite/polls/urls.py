from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('presidential-race/', views.president_2024, name='president-race')
]
