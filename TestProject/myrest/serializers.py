from rest_framework import serializers
from tickets.models import *

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields ='__all__'

class AdminCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminComment
        fields ='__all__'

