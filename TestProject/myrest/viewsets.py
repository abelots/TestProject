from rest_framework import viewsets
from myrest.serializers import TicketSerializer,AdminCommentSerializer,UserSerializer,AdminCommentSerializer,UserCommentSerializer
from tickets.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import filters

class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    model = Ticket
    serializer_class = TicketSerializer

    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)

    ordering = ('-create_date','status')

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.all().filter(user = self.request.user)

        return queryset

    def perform_create(self, serializer):

        return serializer.save(user=self.request.user)



class AdminCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('ticket',)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UserCommentViewSet(viewsets.ModelViewSet):
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('ticket',)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
