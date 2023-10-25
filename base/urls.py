from rest_framework.routers import SimpleRouter
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_info, name="home"),
    path("about/", views.about_info, name="about"),
    path("projects/", views.projects_list, name="projects"),
    path(
        "projects/<str:category>/",
        views.filtered_projects_list,
        name="filtered_projects",
    ),
]