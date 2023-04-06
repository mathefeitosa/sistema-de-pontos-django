from django.urls import path
from . import views


urlpatterns = [
    path("", views.workplaces, name="workplaces"),
    path("create/", views.create_workplace, name="create_workplaces"),
]
