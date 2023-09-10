from rest_framework import serializers


def clean_email(value):
    if "admin" in value:
        raise serializers.ValidationError("admin word should not be in email")


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if value == "admin":
            raise serializers.ValidationError("username can not be 'admin'")

        return value

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("passwords must match")
        return data
