from django.views.generic import TemplateView, ListView, DetailView

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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


def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["ttson.cs@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "pages/contact.html", {"form": form})


def successView(request):
    return HttpResponse("Success! Thank you for your message.")
