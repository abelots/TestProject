from rest_framework import viewsets
from myrest.serializers import TicketSerializer,AdminCommentSerializer
from tickets.models import *


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-create_date')
    serializer_class = TicketSerializer

class AdminCommentViewSet(viewsets.ModelViewSet):
    queryset = AdminComment.objects.all().order_by('-create_date')
    serializer_class = AdminCommentSerializer
