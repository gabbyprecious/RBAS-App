import django.contrib.auth.password_validation as validators
from django.contrib.auth import get_user_model
from django.core import exceptions
from rest_framework import serializers

User = get_user_model()

class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    level = serializers.IntegerField(required=False)
    password = serializers.CharField(trim_whitespace=False)

    def validate_email(self, email):
        """
        Raises exception if email already exist
        :return:
        """
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                raise serializers.ValidationError("user with that email already exists")
        except User.DoesNotExist:
            return email
        return email

    def create(self, validated_data):
        """
        Create the user at DB level
        :param validated_data:
        :return:
        """
        level = validated_data.get("level")
        email = validated_data.get("email")
        self.validate_email(email)
        if level > 4:
            raise serializers.ValidationError("level does not exist")
        user = User.objects.create_user(**validated_data)
        if user.level == 0:
            user.is_superuser = True
        elif user.level == 2 or user.level == 3:
            user.is_superuser = False
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("groups", "user_permissions", "last_login", "password",)