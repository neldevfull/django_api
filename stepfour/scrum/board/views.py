from rest_framework import authentication, permissions, viewsets
from .serializers import SprintSerializer


class DefaultsMixin(object):
    """Settigns default for authentication and permissions, filter and pagination"""

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