from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from wkhtmltopdf.views import PDFTemplateView

from . import views

urlpatterns = [
                  # post views
                  path('', views.page, name='fihrist'),
                  path('ara/', views.results, name='results'),
                  path('ara/sec/', views.sec, name='sec'),
                  path('ekle/', views.ekle, name='ekle'),
                  path('pdf/', views.pdf, name='pdf'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
