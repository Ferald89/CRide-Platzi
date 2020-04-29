"""Users URLs."""

#django
from django.urls import path,include

from rest_framework.routers import DefaultRouter

#View
from .views import users as user_view

router = DefaultRouter()
router.register(r'users',user_view.UserViewSet, basename='users')

urlpatterns=[
        path('',include(router.urls))
]
