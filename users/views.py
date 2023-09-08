import random
from django.conf import settings
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework.permissions import IsAuthenticated

from twilio.rest import Client
from .models import CustomUser, Customer, Vendor
from .serializers import LoginSerializer, RestorePasswordCompleteSerializer, RestorePasswordSerializer, VendorRegisterSerializer, VerifyUserSerializer, CustomerRegisterSerializer, ChangePasswordSerializer


class VendorRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VendorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            phone = request.data['phone']
            user = CustomUser.objects.filter(is_active=True, phone=phone).first()
            if user is not None:
                raise ValidationError("This phone number is already in use.")
            else:
                code = random.randint(1000, 999999)
                vendor = Vendor.objects.create(
                    name=request.data['name'],
                    phone=phone,
                    description=request.data['description'],
                    # ava=request.data['ava'],
                    activation_code=code,
                    is_Vendor=True,
                    is_active=False
                )
                twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                twilio_client.messages.create(
                    to=phone,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=f'Ваш проверочный код: {code}'
                )
                vendor.set_password(request.data['password'])
                vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerRegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomerRegisterSerializer(data=request.data)
        if serializer.is_valid():
            phone = request.data['phone']
            user = CustomUser.objects.filter(is_active=True, phone=phone).first()
            if user is not None:
                raise ValidationError("This phone number is already in use.")
            else:
                code = random.randint(1000, 999999)
                vendor = Customer.objects.create(
                    name=request.data['name'],
                    phone=phone,
                    # ava=request.data['ava'],
                    activation_code=code,
                    is_active=False
                )
                twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                twilio_client.messages.create(
                    to=phone,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=f'Ваш проверочный код: {code}'
                )
                vendor.set_password(request.data['password'])
                vendor.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class VerifyUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(activation_code=request.data['activation_code'])
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UpdateTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

class RestorePasswordAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RestorePasswordSerializer(data=request.data)
        if serializer.is_valid():
            phone = request.data['phone']
            user = CustomUser.objects.filter(is_active=True, phone=phone).first()
            if user is not None:
                code = random.randint(1000, 999999)
                twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                twilio_client.messages.create(
                    to=phone,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=f'Ваш проверочный код: {code}'
                )
                user.activation_code=code
                user.save()
                return Response({'msg': 'Activation code successfully sent'}, status=status.HTTP_200_OK)
            else:
                raise ValidationError("This phone number NOT in use.")
        

class RestorePasswordComplete(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RestorePasswordCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            user = CustomUser.objects.get(phone=request.data['phone'], activation_code=request.data['otp'])
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Password successfully changed'}, status=status.HTTP_200_OK)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response({'msg': 'Password successfully changed'}, status=status.HTTP_200_OK)
        

class ResendActivationCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        phone = data['phone']
        print(phone)
        try:
            user = CustomUser.objects.get(phone=phone)
            if user.is_active:
                return Response({'msg':'User is already verified'})
            code = random.randint(1000, 999999)
            twilio_client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            twilio_client.messages.create(
                to=phone,
                from_=settings.TWILIO_PHONE_NUMBER,
                body=f'Ваш проверочный код: {code}'
            )
            user.activation_code=code
            user.save()
            return Response({'msg':'The verification email has been sent'}, status=status.HTTP_201_CREATED)
        except CustomUser.DoesNotExist:
            return Response({'msg':'No such user, register first'})