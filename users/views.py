from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer


class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'User Registered',

                'refresh': str(refresh),

                'access': str(refresh.access_token)
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(

            username=username,

            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'Login Successful',

                'refresh': str(refresh),

                'access': str(refresh.access_token)
            })

        return Response({

            'error': 'Invalid Credentials'

        }, status=status.HTTP_401_UNAUTHORIZED)