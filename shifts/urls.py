from django.urls import path
from . import views


urlpatterns = [
    path("", views.shifts, name="shifts"),
    path("close/<str:id>", views.close_shift_id, name="close_shift_id"),
    path("close/", views.close_shift, name="close_shift"),
    path("create/", views.create_shift, name="create_shift"),


]
