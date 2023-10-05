from django.urls import path
from .views import (
    HomePageView,
    AboutMePageView,
    WorksPageView,
    BlogPageView,
    BlogDetailPageView,
    RobotsTxtView,
    ContactPageView,
    SuccessPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutMePageView.as_view(), name="about"),
    path("works/", WorksPageView.as_view(), name="works"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<slug:slug>/", BlogDetailPageView.as_view(), name="post_detail"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("success/", SuccessPageView.as_view(), name="success"),
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
]
