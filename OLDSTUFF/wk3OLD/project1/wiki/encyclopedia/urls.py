from django.urls import path, include
import re
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<title>/', views.entry, name="entry"),
    path('search/', views.search, name="search"),
    path('new_page/', views.new_page, name='new_page'),
]
