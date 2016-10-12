from rest_framework import viewsets
from myrest.serializers import TicketSerializer,AdminCommentSerializer,UserSerializer
from tickets.models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import  CreateAPIView
from django.contrib.auth import get_user_model



class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ticket.objects.all().order_by('-create_date')
    serializer_class = TicketSerializer

class AdminCommentViewSet(viewsets.ModelViewSet):
    queryset = AdminComment.objects.all().order_by('-create_date')
    serializer_class = AdminCommentSerializer

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
