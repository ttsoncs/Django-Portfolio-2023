from django.urls import path
from .views import (
    HomePageView,
    AboutMePageView,
    WorksPageView,
    BlogPageView,
    BlogDetailPageView,
    RobotsTxtView,
    contactView,
    successView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutMePageView.as_view(), name="about"),
    path("works/", WorksPageView.as_view(), name="works"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<slug:slug>/", BlogDetailPageView.as_view(), name="post_detail"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
]
