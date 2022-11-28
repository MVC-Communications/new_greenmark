from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    # path("iso_start", views.iso_start, name="iso_start"),
    # path("iso_step_one", views.iso_step_one, name="iso_one"),
    path("iso_buss_info", views.iso_buss_info, name="iso_buss_info"),
    path("iso_step_two", views.iso_step_two, name="iso_step_two"),
    path("iso_step_three", views.iso_step_three, name="iso_step_three"),
    path("iso_step_four", views.iso_step_four, name="iso_step_four"),
    path("print_doc", views.print_doc, name="print_doc"),
    path("view_plan", views.view_plan, name="view_plan"),
    path("view_do", views.view_do, name="view_do"),
    path("view_check", views.view_check, name="view_check"),
    path("view_act", views.view_act, name="view_act"),
]