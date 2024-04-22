from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from post.api.paginations import PostPagination
from post.api.serializers import PostSerializer, PostUpdateCreateSerializer
from post.models import Post
from rest_framework.permissions import (
IsAuthenticated
)
from post.api.permissions import IsOwnerOrAdmin


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = Post.objects.filter(draft=False)
        return queryset


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrAdmin]

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrAdmin]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
