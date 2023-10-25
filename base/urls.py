from rest_framework.routers import SimpleRouter
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("home/", views.home_info, name="home"),
    path("about/", views.about_info, name="about"),
    path("projects/", views.projects_list, name="projects"),
    path(
        "projects/<str:category>",
        views.filtered_projects_list,
        name="filtered_projects",
    ),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
