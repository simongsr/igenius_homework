#!/usr/bin/env python3

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)

from django.urls import path

from homework import views

urlpatterns = [
    path('convert', views.convert),
]
