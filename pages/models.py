from django.db import models
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    tech = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
