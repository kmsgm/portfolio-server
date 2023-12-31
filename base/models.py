from django.db import models


def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)


class Home(models.Model):
    """
    Home Model

        # Fields
        title (str): title of Home.
        subtitle (str): subtitletle of Home.
        description (str): description of Home.
    """

    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class About(models.Model):
    """
    About Model

        # Fields

        description (str): description of About.
        image (image): image of About.
    """

    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    """
    Project Model

        # Fields
        category (str): category of Projects.
        title (str): title of Projects.
        period (str): period of Projects.
        description (str): description of Projects.
        stack (str): stack of Projects.
        image_tag (str): image tag for Projects images.
    """

    category = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    stack = models.CharField(max_length=100, blank=True)
    image_tag = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.title