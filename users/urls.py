from django.urls import path
from .views import VendorRegisterAPIView, CustomerRegisterAPIView, VerifyUserAPIView, LoginView, LogoutAPIView, RestorePasswordAPIView, RestorePasswordComplete, ChangePasswordAPIView, ResendActivationCodeAPIView

urlpatterns = [
    path('user_activation/', VerifyUserAPIView.as_view(), name='user-activation'),
    path('login_user/', LoginView.as_view(), name='user-login'),
    path('logout_user/', LogoutAPIView.as_view(), name='user-login'),
    path('restore_user/', RestorePasswordAPIView.as_view(), name='restore-send-sms'),
    path('restore_complete_user/', RestorePasswordComplete.as_view(), name='restore-complete'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change-passwrod'),
    path('resend_activation_code/', ResendActivationCodeAPIView.as_view(), name='resend-activation-code'),

    path('register_vendor/', VendorRegisterAPIView.as_view(), name='vendor-register'),

    path('register_customer/', CustomerRegisterAPIView.as_view(), name='customer-register'),
]
