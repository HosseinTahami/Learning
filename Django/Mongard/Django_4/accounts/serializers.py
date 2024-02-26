# REST Framework Imports

from rest_framework import serializers

# Django Imports

from django.contrib.auth.models import User


''' First Type of Validation in DRF
    Put the name of function inside a list
    and send it in the specific field as an
    Argument named 'validator'
'''


def clean_email(email):
    if 'admin' in email:
        raise serializers.ValidationError("'admin' can not be in email..!")


class UserRegisterSerializer(serializers.Serializer):

    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[clean_email])
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    ''' Second Type of validator is a function 
        inside the class and it is called validate_fieldname
    '''

    def validate_username(self, username):
        if username == 'admin':
            raise serializers.ValidationError("username can not be 'admin'..!")
        return username

    ''' Third Type of validators is a function with the name
        of validate and does not belong to any specific field
    '''

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match..!")
        return data


class OtherUserRegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

        extra_kwargs = {
            'email':
            {
                'validators': (clean_email,),
                'required': True
            },
            'password':
            {
                'write_only': True,
            },
            'username':
            {
                'required': True,
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        """ If you want to unpack the validated_data dictionary
            with **, then before that you should delete the confirm_password
            inside it because when you are using create_user there is only
            username, email and password..!
        """
        del validated_data['confirm_password']
        return User.objects.create_user(**validated_data)

    def validate_username(self, username):
        if username == 'admin':
            raise serializers.ValidationError(
                '`admin` can not be a username..!')
        return username

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Password must match..!")
        return data
