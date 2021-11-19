from django.urls import path
from api.coronavstech import fibonacci_api

from api.coronavstech.fibonacci_api import views

app_name = 'fibonacci_api'
urlpatterns = [
    path('', views.index, name='index'),
]
