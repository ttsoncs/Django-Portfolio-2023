from django.views.generic import TemplateView, ListView, DetailView

from .models import Project, Post


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutMePageView(TemplateView):
    template_name = "pages/about_me.html"


class WorksPageView(ListView):
    model = Project
    template_name = "pages/works.html"


class BlogPageView(ListView):
    model = Post
    template_name = "pages/blog.html"


class BlogDetailPageView(DetailView):
    model = Post
    template_name = "pages/blog_detail.html"


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
