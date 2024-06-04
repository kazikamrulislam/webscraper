from django.urls import path
from .views import scraping_run

urlpatterns = [
    path('scraping_run/', scraping_run, name='scraping_run'),
]