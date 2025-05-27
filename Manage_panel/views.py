from django.shortcuts import render, redirect
from Ticket_system.forms import TicketForm
from Ticket_system.models import Ticket, Status


def home(request):
    tickets = Ticket.objects.all()
    tickets_count = Ticket.objects.all().count()
    form = TicketForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ticket = form.save(commit=False)
            default_status = Status.objects.get(title='Nowy')
            ticket.status = default_status
            ticket.save()
            return redirect('home')
    return render(request, 'home.html', {'tickets': tickets, 'form': form, 'tickets_count': tickets_count})
