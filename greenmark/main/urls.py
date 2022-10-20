from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("iso_step_one", views.iso_step_one, name="iso_one"),
    path("print_doc", views.print_doc, name="print_doc"),
]