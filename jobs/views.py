from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models import Job

from .serializers import JobSerializer

from employer.models import EmployerProfile


class JobListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        jobs = Job.objects.all()

        serializer = JobSerializer(
            jobs,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        if request.user.role != 'employer':

            return Response({

                'error': 'Only employers can create jobs'

            }, status=status.HTTP_403_FORBIDDEN)

        try:

            employer_profile = EmployerProfile.objects.get(
                user=request.user
            )

        except EmployerProfile.DoesNotExist:

            return Response({

                'error': 'Employer profile not found'

            }, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        data['employer'] = employer_profile.id

        serializer = JobSerializer(
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


class JobDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):

        try:

            return Job.objects.get(pk=pk)

        except Job.DoesNotExist:

            return None

    def get(self, request, pk):

        job = self.get_object(pk)

        if job is None:

            return Response({

                'error': 'Job not found'

            }, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(job)

        return Response(serializer.data)

    def put(self, request, pk):

        job = self.get_object(pk)

        if job is None:

            return Response({

                'error': 'Job not found'

            }, status=status.HTTP_404_NOT_FOUND)

        serializer = JobSerializer(
            job,
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

    def delete(self, request, pk):

        job = self.get_object(pk)

        if job is None:

            return Response({

                'error': 'Job not found'

            }, status=status.HTTP_404_NOT_FOUND)

        job.delete()

        return Response({

            'message': 'Job deleted successfully'

        })