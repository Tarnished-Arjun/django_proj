from django.urls import path

from .views import CandidateProfileView,CandidateListView

urlpatterns = [
    path(
        'profile/',
        CandidateProfileView.as_view(),
        name='candidate-profile'
    ),

    path(
        "all/",
        CandidateListView.as_view(),
        name="candidate-list"
    ),

]