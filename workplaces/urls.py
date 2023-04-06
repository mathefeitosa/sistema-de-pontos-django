from django.urls import path
from workplaces import views


urlpatterns = [
    path("", views.workplaces, name="workplaces"),
    path("create/", views.create_workplaces, name="create_workplaces"),
]
