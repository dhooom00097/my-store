"""
URL configuration for neom project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Project apps
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
]
