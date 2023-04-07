from django.urls import path
from profiles import views


urlpatterns = [
    path("", views.profiles, name="profiles"),
    path('login/', views.login_page, name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("create_user/", views.create_user, name="create_user"),
    path("edit/<str:id>", views.edit_profile, name="edit_profile"),
]
