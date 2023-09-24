from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import FAQ


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutMePageView(TemplateView):
    template_name = "pages/about_me.html"

    def get_context_data(self, **kwargs):
        context = super(AboutMePageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class WorksPageView(TemplateView):
    template_name = "pages/works.html"


class BlogPageView(TemplateView):
    template_name = "pages/blog.html"


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
