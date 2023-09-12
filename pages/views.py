from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "_base.html"


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
