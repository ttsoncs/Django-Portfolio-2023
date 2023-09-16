from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import FAQ


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class AboutMePageView(TemplateView):
    template_name = "pages/about_me.html"

    def get_context_data(self, **kwargs):
        context = super(AboutMePageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class WorksPageView(TemplateView):
    template_name = "pages/works.html"

    def get_context_data(self, **kwargs):
        context = super(WorksPageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class BlogPageView(TemplateView):
    template_name = "pages/blog.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context["faq_list"] = FAQ.objects.all()
        return context


class RobotsTxtView(TemplateView):
    template_name = "robots.txt"
