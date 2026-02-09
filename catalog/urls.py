from django.urls import path
from . import views
from .views import catalog_view
urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', catalog_view, name='catalog'),
]



