from typing import Any
from django.views.generic import View, TemplateView, ListView, DetailView

from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

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


class ContactPageView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "pages/contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            user_email = form.cleaned_data["user_email"]
            user_subject = form.cleaned_data["user_subject"]
            user_message = f'From: {user_email} \nMessage: {form.cleaned_data["user_message"]}'
            my_email = settings.DEFAULT_FROM_EMAIL
            my_subject = "Thank You for Reaching Out"
            my_message = f"Dear {user_name},\n\nThank you for contacting me through my portfolio. I wanted to acknowledge that I have received your message and will be responding to you shortly.\n\nI appreciate your interest and patience as I review your inquiry. I understand the importance of your message and will provide a prompt and thorough response.\n\nThank you for considering my portfolio, and I look forward to assisting you further.\n\nBest regards,\n\nSơn"
            try:
                send_mail(user_subject, user_message, my_email, [my_email])
                send_mail(my_subject, my_message, my_email, [user_email])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
        return render(request, "pages/contact.html", {"form": form})

class SuccessPageView(TemplateView):
    template_name = "pages/success.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["api"] = settings.EMAIL_HOST_PASSWORD
        return context        
