
from django.shortcuts import render
from tickets.models import *

#def index(request):
 #   return render('ticket.html')

def ticket(request,ticket_id):
    return render(request, 'ticket.html')

def tickets(request):
    ticket = Ticket.objects.all()
    new_tickets = ticket.order_by('-create_date')[0:20]

    return render(request, 'ticket_list.html',{'new_tickets': new_tickets})