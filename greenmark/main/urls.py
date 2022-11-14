from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("iso_start", views.iso_start, name="iso_start"),
    path("iso_step_one", views.iso_step_one, name="iso_one"),
    path("iso_buss_info", views.iso_buss_info, name="iso_buss_info"),
    path("print_doc", views.print_doc, name="print_doc"),
]