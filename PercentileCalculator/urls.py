
from django.urls import path
from . import views

urlpatterns = [
    path('',views.calculatePercentile,name='calculatePercentile')
]
