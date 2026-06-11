from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import EmployerProfile
from .serializers import EmployerProfileSerializer

class EmployerProfileView(
generics.GenericAPIView
):


 serializer_class = EmployerProfileSerializer

permission_classes = [IsAuthenticated]

def get(self, request):

    profile = EmployerProfile.objects.get(
        user=request.user
    )

    serializer = self.get_serializer(
        profile
    )

    return Response(serializer.data)

def post(self, request):

    serializer = self.get_serializer(
        data=request.data
    )

    serializer.is_valid(
        raise_exception=True
    )

    serializer.save(
        user=request.user
    )

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )

def put(self, request):

    profile = EmployerProfile.objects.get(
        user=request.user
    )

    serializer = self.get_serializer(
        profile,
        data=request.data,
        partial=True
    )

    serializer.is_valid(
        raise_exception=True
    )

    serializer.save()

    return Response(serializer.data)

