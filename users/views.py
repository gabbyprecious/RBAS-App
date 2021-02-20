from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet

from users.serializers import SignUpSerializer, UserSerializer

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.data["username"])
        if user.check_password(request.data["password"]):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'user_level': user.level
            })
        else:
            return Response({"error": "Invalid Username or Password", "success": False}, status=status.HTTP_401_UNAUTHORIZED)


class SignUpView(GenericViewSet):

    def create(self, request):
        """
        Create User,
        """

        serializer = SignUpSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"error": serializer.errors, "success": False}, status=status.HTTP_403_FORBIDDEN)
        user = serializer.save()
        user_serializer = UserSerializer(user)

        return Response(
            {"user": user_serializer.data, "success": True},
            status=status.HTTP_201_CREATED,
        )

