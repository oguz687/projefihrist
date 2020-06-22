from django.urls import path
from . import views
from .views import PersonelView

urlpatterns = [
 # post views
 path('', PersonelView.as_view(), name='fihrist'),
 path('<str:personel>/', PersonelView.as_view(), name='results'),

]