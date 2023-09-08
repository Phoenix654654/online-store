from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser, Vendor


class VendorRegisterSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(required=True, validators=[UniqueValidator(queryset=Vendor.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Vendor
        fields = [
            'id',
            'phone',
            'name',
            'description',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': "Password fields didn`t match."}
            )
        return attrs
    

class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Vendor
        fields = [
            'id',
            'phone',
            'name',
            'password',
            'password2',
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': "Password fields didn`t match."}
            )
        return attrs


class VerifyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['activation_code',]


class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone', 'password']

    def validate_phone(self, phone):
        if not CustomUser.objects.filter(phone=phone).exists():
            raise serializers.ValidationError('Пользователь с указанным номером не зарегистрирован')
        return phone
    
    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
        user = CustomUser.objects.get(phone=phone)
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный пароль')
        return super().validate(attrs)


class RestorePasswordSerializer(serializers.Serializer):

    class Meta:
        model = CustomUser
        fields = ['phone', ]


class RestorePasswordCompleteSerializer(serializers.Serializer):
    phone = PhoneNumberField()
    otp = serializers.CharField(max_length=6, min_length=4)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'otp', 'password', 'password2']

    def validate(self, attrs):
        phone_number=attrs.get('phone')
        code=attrs.pop('otp')
        password=attrs.get('password')
        password2=attrs.pop('password2')
        print(f"Phone: {phone_number}, Code: {code}")
        if not CustomUser.objects.filter(phone=phone_number, activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не найден')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm password do not match")
        return attrs
    
    def set_new_password(self):
        phone = self.validated_data.get('phone')
        password = self.validated_data.get('password')
        user = CustomUser.objects.get(phone=phone)
        user.set_password(password)
        user.save()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['old_password', 'password', 'password2']

    def validate_old_password(self, password):
        user = self.context['request'].user
        if not user.check_password(password):
            raise serializers.ValidationError('Wrong password')
        return password
    
    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm password does not match")
        return attrs
    
    def set_new_password(self):
        user = self.context['request'].user
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()