from django.urls import path
from .views import (
    HomePageView,
    AboutMePageView,
    WorksPageView,
    BlogPageView,
    BlogDetailPageView,
    RobotsTxtView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutMePageView.as_view(), name="about"),
    path("works/", WorksPageView.as_view(), name="works"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<slug:slug>/", BlogDetailPageView.as_view(), name="post_detail"),
    path("robots.txt", RobotsTxtView.as_view(content_type="text/plain"), name="robots"),
]
