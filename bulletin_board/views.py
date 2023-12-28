from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from bulletin_board.filters import AdFilter
from bulletin_board.models import Ad, Comment
from bulletin_board.paginator import AdPaginator
from bulletin_board.permissions import IsAdmin, IsAuthor
from bulletin_board.serliazers import (AdDetailSerializer, AdSerializer,
                                       CommentSerializer)


class AdCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания объявления"""
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


class AdListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра списка объявлений"""
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_queryset(self):
        queryset = Ad.objects.all().order_by('-created_at')
        return queryset


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor or IsAdmin]


class AdDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления привычки"""
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor or IsAdmin]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        ad_pk = self.kwargs.get('pk')
        print(ad_pk)
        queryset = Comment.objects.filter(ad=ad_pk)
        return queryset

    def perform_create(self, serializer, *args, **kwargs):
        new_comment = serializer.save()
        new_comment.author = self.request.user
        ad_pk = self.kwargs.get('pk')
        new_comment.ad = Ad.objects.get(pk=ad_pk)
        new_comment.save()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list' or \
                self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy' or \
                self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]
        return [permission() for permission in permission_classes]
