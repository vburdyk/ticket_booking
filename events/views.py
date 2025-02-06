from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect

from events.models import Event


def user_is_admin_or_organizer(user):
    return user.groups.filter(name='Administrator').exists() or user.groups.filter(name='Organizer').exists()


@login_required(login_url='signin')
@user_passes_test(user_is_admin_or_organizer, login_url='index')
def event_create_view(request):
    return render(request, 'create_event.html')


@login_required(login_url='signin')
@user_passes_test(user_is_admin_or_organizer, login_url='index')
def event_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        datetime = request.POST.get('datetime')
        location = request.POST.get('location')
        image = request.FILES.get('image')
        organizer = request.user

        event = Event.objects.create(
            title=title,
            description=description,
            datetime=datetime,
            location=location,
            image=image,
            organizer=organizer,

        )
        event.save()

        messages.success(request, 'Event created!')
        return redirect('index')
