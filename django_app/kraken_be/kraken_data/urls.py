from django.urls import path
from . import views
from django.views.generic import TemplateView


#--------------------------------------------------------------
urlpatterns = [
    path('', views.home, name='home'),
    path('get-ohlc-data/', views.get_ohlc_data, name='get_ohlc_data'),
    path('chart/', TemplateView.as_view(template_name='index.html'))
]