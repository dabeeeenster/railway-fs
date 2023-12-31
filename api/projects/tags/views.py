from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from projects.permissions import VIEW_PROJECT

from . import serializers
from .models import Tag
from .permissions import TagPermissions


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TagSerializer
    permission_classes = [IsAuthenticated, TagPermissions]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Tag.objects.none()

        project = get_object_or_404(
            self.request.user.get_permitted_projects(VIEW_PROJECT),
            pk=self.kwargs["project_pk"],
        )
        queryset = project.tags.all()

        return queryset

    def perform_create(self, serializer):
        project_id = self.kwargs["project_pk"]
        serializer.save(project_id=project_id)

    def perform_update(self, serializer):
        project_id = self.kwargs["project_pk"]
        serializer.save(project_id=project_id)
