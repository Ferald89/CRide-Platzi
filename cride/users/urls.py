"""Users URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# View
from .views import users as user_view

router = DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='users')

urlpatterns = [
        path('', include(router.urls))
        ]
