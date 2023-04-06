from django.urls import path
from profiles import views


urlpatterns = [
    path("", views.profiles, name="profiles"),
    path('login/', views.login_page, name='login'),
    path("create/", views.create_profile, name="create_profiles"),
]
