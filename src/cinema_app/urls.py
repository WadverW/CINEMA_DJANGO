from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("lte-admin/", views.lte_admin, name="lte_admin"),
]
