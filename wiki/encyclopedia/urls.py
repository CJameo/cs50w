from django.urls import path

from . import views

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>/", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.update, name="update"),
    path("wiki/<title>/edit/", views.entry, name="edit"),
    path("random/", views.random, name="random")
]
