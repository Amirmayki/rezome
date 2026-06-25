from django.urls import path

from . import views

urlpatterns = [

    path("login/", views.login_view, name="login"),

    path("register/", views.register_view, name="register"),

    path("profile/", views.profile, name="profile"),

    path("dashboard/", views.dashboard, name="dashboard"),

]