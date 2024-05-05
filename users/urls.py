from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("signup/", views.register_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("change-pass/", views.change_user_pass, name="change_pass"),
    path("change-pass-2/", views.change_pass_without_pass, name="change_pass_2"),
]
