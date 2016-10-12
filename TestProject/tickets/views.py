from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import render,redirect
from tickets.models import *

from forms import AdminCommentForm,CommentForm,UserCommentForm




def tickets(request, page_number=1):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        if request.user.is_staff:
            ticket = Ticket.objects.all()
            ticket = ticket.order_by('-create_date')
            current_page = Paginator(ticket,2)
            return render(request, 'admin_ticket_list.html',{'tickets': current_page.page(page_number)})
        else:
            ticket = request.user.ticket.all()
            ticket = ticket.order_by('-create_date')
            current_page = Paginator(ticket,2)
            return render(request, 'ticket_list.html',{'tickets': current_page.page(page_number)})

def ticket(request, ticket_id=1,page_number=1):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        comment_form = CommentForm
        args = {}
        args['ticket'] = Ticket.objects.get(id=ticket_id)
        admin_comments = args['ticket'].admincomments.all().order_by('-create_date')
        user_comments = args['ticket'].usercomments.all().order_by('-create_date')
        comments = list(admin_comments) + list(user_comments)
        comments.sort(key=lambda x: x.create_date)
        current_page = Paginator(comments, 2)
        args['comments'] = current_page.page(page_number)
        args['form'] = comment_form
        if request.user.is_staff:
            return render(request,'admin_ticket.html', args)
        else:
            return render(request,'ticket.html', args)


def addcomment(request, ticket_id):
    if request.POST:
        if  request.user.is_staff:
            form = AdminCommentForm(request.POST, request.FILES or None)
        else:
            form = UserCommentForm(request.POST, request.FILES or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = Ticket.objects.get(id=ticket_id)
            comment.user = User.objects.get(id=1)
            if request.FILES.has_key('attached_file'):
                comment.attached_file = request.FILES['attached_file']
            else:
                comment.attached_file = None
            form.save()
    admin_comments_count = Ticket.objects.get(id=ticket_id).admincomments.all().count()
    user_comments_count = Ticket.objects.get(id=ticket_id).usercomments.all().count()
    page = admin_comments_count + user_comments_count
    page = (page - 1) / 2 + 1

    return redirect('/ticket/'+ ticket_id+'/'+str(page))

def changestatus(request, ticket_id,page_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = not ticket.status
    ticket.save()

    return redirect('/tickets/'+str(page_id))
