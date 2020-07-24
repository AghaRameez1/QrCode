import json

from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from api.Serializers.user_serializers import UserSerializer, UserProfileSerializer, UserAuthSerializer, \
    UserRegisterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# ViewSets define the view behavior.
from api.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.

class UserProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserRegistration(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', False)
        password = request.data.get('password', False)
        confirm_password = request.data.get('confirm_password',False)
        name = request.data.get('name', False)

        if username and password and confirm_password:
            if password == confirm_password:
                temp_data ={
                    'username': username,
                    'password': password,
                    'name': name
                }
                serializer = UserRegisterSerializer(data=temp_data)
                created= serializer.registerUser(data=temp_data)
                print(created)
                if created['created'] == True:
                    return Response({
                    'status': status.HTTP_200_OK,
                        'data':'Your Auth Token is: '+created['key']
                    })
                else:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'data': 'User already exist'
                    })
            else:
                return Response({
                    'status': status.HTTP_400_BAD_REQUEST,
                    'data':'Passwords do not match'
                })
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST
            })

class UserAuthentication(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username',False)
        password = request.data.get('password',False)
        if username and password:
            temp_data = {
                'username': username,
                'password': password
            }
            serializer = UserAuthSerializer(data=temp_data)
            status_obj = serializer.validateUser(data=temp_data)
            # print(serializer)
            if status_obj == True:
                return Response({
                'status': status.HTTP_200_OK,
                'data': status_obj
            })
            else:
                return Response({
                    'status':status.HTTP_401_UNAUTHORIZED,
                    'data':'Invalid'
                })
        else:
            return Response({
                'status':status.HTTP_400_BAD_REQUEST,
                'data':'Missing Credentials'
            })