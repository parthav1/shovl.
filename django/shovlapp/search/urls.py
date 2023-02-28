from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='search-index'),
    path('arvr/', views.arvr, name='search-arvr'),
    path('ai/', views.ai, name='search-ai'),
    path('bigdata/', views.bigdata, name='search-bigdata'),
    path('blockchain/', views.blockchain, name='search-blockchain'),
    path('cloud/', views.cloud, name='search-cloud'),
    path('cybersecurity/', views.cybersecurity, name='search-cybersecurity'),
    path('ecommerce/', views.ecommerce, name='search-ecommerce'),
    path('iot/', views.iot, name='search-iot'),
    path('it/', views.it, name='search-it'),
    path('softwaredev/', views.softwaredev, name='search-softwaredev'),
    path('softwaretesting/', views.softwaretesting, name='search-softwaretesting'),
    path('webdev/', views.webdev, name='search-webdev'),
    path('invalid/', views.invalid, name='search-invalid'),
    path('results/', views.results, name='results')
]