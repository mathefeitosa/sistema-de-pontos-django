from django.urls import path
from profiles import views


urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("create/", views.create_profile, name="create_profiles"),
]
