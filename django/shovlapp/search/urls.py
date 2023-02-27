from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='search-index'),
    path('results/', views.results, name='search-results'),
]