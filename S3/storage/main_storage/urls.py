from django.urls import path

from .views import DataAPI


urlpatterns = [
    path("modeling/", DataAPI.as_view()),
]
