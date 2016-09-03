from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from .models import Strint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer


User = get_user_model()


class DefaultsMixin(object):
    """Settigns default for authentication, permissions, filters and pagination"""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )

    permission_class = (
        permissions.isAuthenticated,
    )

    paginate_by = 50
    paginate_by_param = 'page_size'
    max_paginate_by = 50


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for list and create sprints"""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for list and create tasks"""

    queryset = Task,object.all()
    serializer_class = TaskSerializer


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for list users"""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer