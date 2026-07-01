from django.urls import path

from .views import EmployerProfileView,EmployerListView

urlpatterns = [

    path(
        'profile/',
        EmployerProfileView.as_view(),
        name="employer-profile"
    ),

     path(
        "all/",
        EmployerListView.as_view(),
        name="employer-list"
    ),

]