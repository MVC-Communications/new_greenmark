from django.urls import path
from . import views

app_name = "accounts"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("admin-dashboard", views.admin_dashboard, name="admin-dashboard"),
    path("admin/view_iso/<int:pk>", views.admin_view_iso, name="admin_view_iso"),
]
