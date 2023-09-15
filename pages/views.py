from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import FAQ


class HomePageView(ListView):
    template_name = "pages/home.html"
    model = FAQ


class AboutMePageView(ListView):
    template_name = "pages/about_me.html"
    model = FAQ


class WorksPageView(ListView):
    template_name = "pages/works.html"
    model = FAQ


class BlogPageView(ListView):
    template_name = "pages/blog.html"
    model = FAQ


class ContactPageView(ListView):
    template_name = "pages/contact.html"
    model = FAQ


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
