from django.urls import path
from . import views

urlpatterns = [
 # post views
 path('', views.page, name='fihrist'),
 path('search/', views.results, name='results'),
 path('search/',views.sec,name='sec'),
]