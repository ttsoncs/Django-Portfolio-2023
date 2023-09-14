from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import FAQ


class HomePageView(ListView):
    template_name = "home.html"
    model = FAQ


class AboutMePageView(ListView):
    template_name = "about_me.html"
    model = FAQ


class WorksPageView(ListView):
    template_name = "works.html"
    model = FAQ


class BlogPageView(ListView):
    template_name = "blog.html"
    model = FAQ


class ContactPageView(ListView):
    template_name = "contact.html"
    model = FAQ


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
