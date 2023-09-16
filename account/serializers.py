from rest_framework import serializers,fields
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()



class UserRegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120,write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            "password",
        ]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializerWithToken(UserRegisterationSerializer):
    token = serializers.SerializerMethodField(read_only=True,source="auth-token")

    class Meta:
        model = User
        fields = [
            "token",
        ]
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)



