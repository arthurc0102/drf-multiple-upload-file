from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import PostSerializers


class PostViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related('attachments')
    serializer_class = PostSerializers
    permission_classes = (AllowAny,)
