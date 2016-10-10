
from django.shortcuts import render,redirect
from tickets.models import *
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404


from forms import CommentForm




def tickets(request, page_number=1):
    try:
        ticket = Ticket.objects.all()
        ticket = ticket.order_by('-create_date')
        current_page = Paginator(ticket,2)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'ticket_list.html',{'tickets': current_page.page(page_number)})




def ticket(request, ticket_id=1,page_number=1):
    comment_form = CommentForm
    args = {}
    args['ticket'] = Ticket.objects.get(id=ticket_id)
    comments = args['ticket'].admincomments.all()
    current_page = Paginator(comments, 2)
    args['comments'] = current_page.page(page_number)
    args['form'] = comment_form
    return render(request,'ticket.html', args)


def addcomment(request, ticket_id):
    if request.POST:
        form = CommentForm(request.POST, request.FILES or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = Ticket.objects.get(id=ticket_id)
            comment.user = User.objects.get(id=1)
            comment.attached_file = request.FILES['attached_file']

            form.save()


        page = AdminComment.objects.filter(ticket_id=ticket_id).count()
        page = (page - 1) / 2 + 1

    return redirect('/ticket/'+ ticket_id+'/'+str(page))