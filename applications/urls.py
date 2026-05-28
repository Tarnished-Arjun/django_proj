from django.urls import path

from .views import (
    ApplyJobView,
    MyApplicationsView,
    JobApplicantsView
)


urlpatterns = [

    path(
        'apply/<int:job_id>/',
        ApplyJobView.as_view()
    ),

    path(
        'my-applications/',
        MyApplicationsView.as_view()
    ),

      path(
        'job/<int:job_id>/applicants/',
        JobApplicantsView.as_view()
    ),

]