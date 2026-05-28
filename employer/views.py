from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models import EmployerProfile

from .serializers import EmployerProfileSerializer


class EmployerProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.user.role != 'employer':

            return Response({

                'error': 'Only employers can create profiles'

            }, status=status.HTTP_403_FORBIDDEN)

        data = request.data.copy()

        data['user'] = request.user.id

        serializer = EmployerProfileSerializer(
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

            profile = EmployerProfile.objects.get(
                user=request.user
            )

            serializer = EmployerProfileSerializer(
                profile
            )

            return Response(serializer.data)

        except EmployerProfile.DoesNotExist:

            return Response({

                'error': 'Employer profile not found'

            }, status=status.HTTP_404_NOT_FOUND)