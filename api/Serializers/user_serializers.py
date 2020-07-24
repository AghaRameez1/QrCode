from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from rest_framework.authtoken.models import Token

from api.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id', 'name']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def registerUser(self, data):
        try:
            user_obj = User.objects.create_user(username=data['username'], email=None, password=data['password'])
            UserProfile.objects.create(user=user_obj, name=data['name'])
            token = Token.objects.create(user=user_obj)
            data = {
                'created': True,
                'key': token.key
            }
            return data
        except Exception as e:
            data = {
                'created': False,
                'error': e
            }
            return data
class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validateUser(self, data):
        if data:
            user_obj = User.objects.get(username=data['username'])
            try:
                pass_obj=user_obj.check_password(data['password'])
                if pass_obj:
                    return True
                else:
                    return ('Invalid')
            except user_obj.DoesNotExist:
                return False
        else:
            return False
