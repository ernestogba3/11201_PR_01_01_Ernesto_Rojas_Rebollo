from django.urls import path

from .views import cv_json_view, cv_view

urlpatterns = [
    path("", cv_view, name="cv-home"),
    path("api/cv/", cv_json_view, name="cv-json"),
]
