# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:02:06 2020

@author: Jaeik
"""

from django.urls import path
from research import views


urlpatterns = [
        path('', views.index, name = 'index'),
    ]