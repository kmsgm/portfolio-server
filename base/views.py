import json
from django.http import JsonResponse
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.serializers import serialize
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Home, About, Project, Image


@api_view(["GET"])
def home_info(request):
    if request.method == "GET":
        home = Home.objects.get(title="Minseo Kim")
        response_dict = {
            "title": home.title,
            "subtitle": home.subtitle,
            "description": home.description,
        }
        return JsonResponse(response_dict, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])


@api_view(["GET"])
def about_info(request):
    if request.method == "GET":
        about = About.objects.get(title="About Me")
        response_dict = {
            "description": about.description,
            "image": json.dumps(str(about.image)),
        }
        return JsonResponse(response_dict, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])


@api_view(["GET"])
def projects_list(request):
    if request.method == "GET":
        projects = Project.objects.all()
        projects_with_images = []

        for project in projects:
            images = project.image_set.all()
            projects_with_images.append(
                {
                    "id": project.id,
                    "category": project.category,
                    "title": project.title,
                    "period": project.period,
                    "description": project.description,
                    "stack": project.stack,
                    "images": [
                        {"id": image.id, "url": image.image.url} for image in images
                    ],
                }
            )

        return JsonResponse(projects_with_images, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])


@api_view(["GET"])
def filtered_projects_list(request, category):
    if request.method == "GET":
        projects = Project.objects.filter(category__iexact=category)
        projects_with_images = []

        for project in projects:
            images = project.image_set.all()
            projects_with_images.append(
                {
                    "id": project.id,
                    "category": project.category,
                    "title": project.title,
                    "period": project.period,
                    "description": project.description,
                    "stack": project.stack,
                    "images": [
                        {"id": image.id, "url": image.image.url} for image in images
                    ],
                }
            )
        return JsonResponse(projects_with_images, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])
