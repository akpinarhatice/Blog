from django.urls import path, include

from post.api.views import PostListAPIView, PostDetailAPIView, \
    PostUpdateAPIView, PostDestroyAPIView, PostCreateAPIView

app_name = 'post'

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('destroy/<slug>', PostDestroyAPIView.as_view(), name='delete'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('create/', PostCreateAPIView.as_view(), name='create')

]
