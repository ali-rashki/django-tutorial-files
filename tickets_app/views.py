from django.shortcuts import render , redirect
from .models import Ticket
# Create your views here.

def add_ticket(request):
    title = request.POST.get('title')
    body = request.POST.get('body')

    if title and body:
        Ticket.objects.create(title=title, body=body)
        return redirect('/tickets/list')
    return render(request, 'tickets_app/add_ticket.html')

def show_all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets_app/detail_ticket.html', {'tickets': tickets})


