from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer

from employer.models import EmployerProfile


class JobListCreateView(
    generics.ListCreateAPIView
):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        if self.request.user.role != 'employer':

            raise PermissionError(
                'Only employers can create jobs'
            )

        employer_profile = EmployerProfile.objects.get(
            user=self.request.user
        )

        serializer.save(
            employer=employer_profile
        )


class JobDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAuthenticated]