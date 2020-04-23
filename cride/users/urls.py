"""Users URLs."""

#django
from django.urls import path

#View
from cride.users.views import (
        AccountVerificationAPIView,
        UserLoginAPIView,
        UserSignUpAPIView,
)

urlpatterns=[
        path('users/login/',UserLoginAPIView.as_view(),name='login'),
        path('users/signup/',UserSignUpAPIView.as_view(),name='signup'),
        path('users/verify/',AccountVerificationAPIView.as_view(),name='verify'),
]
