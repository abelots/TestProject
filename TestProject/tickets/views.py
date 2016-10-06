
from django.shortcuts import render
from tickets.models import *
from django.core.paginator import Paginator

#def index(request):
 #   return render('ticket.html')

def ticket(request,ticket_id):
    return render(request, 'ticket.html')

def tickets(request, page_number=1):
    ticket = Ticket.objects.all()
 #   new_tickets = ticket.order_by('-create_date')[0:20]
    current_page = Paginator(ticket,2)
    return render(request, 'ticket_list.html',{'tickets': current_page.page(page_number)})