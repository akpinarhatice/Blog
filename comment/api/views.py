from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, DestroyAPIView

from comment.api.serializers import CommentCreateSerializer, \
    CommentListSerializer, CommentUpdateDeleteSerializer
from comment.models import Comment

from comment.api.permissions import IsOwner


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent=None)


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
    #comment line


