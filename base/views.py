from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Home, About, Project


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
        }
        return JsonResponse(response_dict, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])


@api_view(["GET"])
def projects_list(request):
    if request.method == "GET":
        projects = [project for project in Project.objects.all().values()]

        return JsonResponse(projects, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])


@api_view(["GET"])
def filtered_projects_list(request, category):
    if request.method == "GET":
        filtered_projects = [project for project in Project.objects.filter(category__iexact=category).values()]

        return JsonResponse(filtered_projects, safe=False)
    else:
        return HttpResponseNotAllowed(["GET"])
