from django.urls import path
from . import views

urlpatterns = [
 # post views
 path('', views.page, name='fihrist'),
 path('search/', views.results, name='results'),
 path('sec/',views.sec,name='sec'),
]