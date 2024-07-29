from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Event, Registration
from .forms import RegistrationForm
from .serializers import EventSerializer, RegistrationSerializer



def event_list(request):
    events = Event.objects.all()
    now = timezone.now()
    return render(request, 'event_list.html', {'events': events, 'now': now})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        print('post edildi')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            print(registration.event)
            print(registration.email)
            if event.registered_count >= event.capacity:
                form.add_error(None, 'Event capacity full')

            elif Registration.objects.filter(event=event, email=registration.email).exists():
                form.add_error(None, 'This email is already registered for the event')
            elif event.date < timezone.now():
                form.add_error(None, 'Üzgünüm,etkinlik tarihini kaçırdın')
            else:
                event.registered_count += 1
                event.save()
                registration.save()
                return redirect('event_list')
    else:
        form = RegistrationForm()
    return render(request, 'event_detail.html', {'event': event, 'form': form})



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:  # Kayıt başarılıysa
            event_id = request.data.get('event')
            event = Event.objects.get(id=event_id)
            event.registered_count += 1
            event.save()
        return response