from django.contrib import admin
from .models import Home, About, Project, Image

admin.site.register(Home)
admin.site.register(About)


class ImageInline(admin.TabularInline):
    model = Image


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Project, ProjectAdmin)
