from django.shortcuts import render
from events.models import Event


def index_view(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})