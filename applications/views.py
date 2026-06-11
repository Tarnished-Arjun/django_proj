from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import JobApplication
from .serializers import JobApplicationSerializer

from candidate.models import CandidateProfile
from jobs.models import Job
from employer.models import EmployerProfile

class ApplyJobView(APIView):


 permission_classes = [IsAuthenticated]

def post(self, request, job_id):

    if request.user.role != 'candidate':

        return Response(
            {
                'error': 'Only candidates can apply for jobs'
            },
            status=status.HTTP_403_FORBIDDEN
        )

    try:

        candidate_profile = CandidateProfile.objects.get(
            user=request.user
        )

    except CandidateProfile.DoesNotExist:

        return Response(
            {
                'error': 'Candidate profile not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

    try:

        job = Job.objects.get(
            id=job_id
        )

    except Job.DoesNotExist:

        return Response(
            {
                'error': 'Job not found'
            },
            status=status.HTTP_404_NOT_FOUND
        )

    already_applied = JobApplication.objects.filter(
        candidate=candidate_profile,
        job=job
    ).exists()

    if already_applied:

        return Response(
            {
                'error': 'Already applied to this job'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    application = JobApplication.objects.create(
        candidate=candidate_profile,
        job=job
    )

    serializer = JobApplicationSerializer(
        application
    )

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )


class MyApplicationsView(
generics.ListAPIView
):


  serializer_class = JobApplicationSerializer

permission_classes = [IsAuthenticated]

def get_queryset(self):

    candidate_profile = CandidateProfile.objects.get(
        user=self.request.user
    )

    return JobApplication.objects.filter(
        candidate=candidate_profile
    )


class JobApplicantsView(
generics.ListAPIView
):


 serializer_class = JobApplicationSerializer

permission_classes = [IsAuthenticated]

def get_queryset(self):

    employer_profile = EmployerProfile.objects.get(
        user=self.request.user
    )

    job = Job.objects.get(
        id=self.kwargs['job_id'],
        employer=employer_profile
    )

    return JobApplication.objects.filter(
        job=job
    )

