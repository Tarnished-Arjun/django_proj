from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import CandidateProfile
from .serializers import CandidateProfileSerializer


class CandidateProfileView(
    generics.RetrieveUpdateAPIView,
    generics.CreateAPIView
):

    serializer_class = CandidateProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return CandidateProfile.objects.get(
            user=self.request.user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )