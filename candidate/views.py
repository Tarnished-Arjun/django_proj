from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import CandidateProfile
from .serializers import CandidateProfileSerializer


class CandidateProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.user.role != 'candidate':
            return Response(
                {'error': 'Only candidates can create profiles'},
                status=status.HTTP_403_FORBIDDEN
            )

        if CandidateProfile.objects.filter(
            user=request.user
        ).exists():

            return Response(
                {'error': 'Profile already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        data = request.data.copy()
        data['user'] = request.user.id

        serializer = CandidateProfileSerializer(
            data=data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request):

        try:

            profile = CandidateProfile.objects.get(
                user=request.user
            )

            serializer = CandidateProfileSerializer(
                profile
            )

            return Response(serializer.data)

        except CandidateProfile.DoesNotExist:

            return Response(
                {'error': 'Profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request):

        try:

            profile = CandidateProfile.objects.get(
                user=request.user
            )

        except CandidateProfile.DoesNotExist:

            return Response(
                {'error': 'Profile not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )