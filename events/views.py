from django.shortcuts import render, redirect
from .models import Event
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        image = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        Event.objects.create(image=image, title=title, description=description)
        return redirect('event_list')
    return render(request, 'events/add_event.html')

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html')
def allevents(request):
       events =Event.objects.all()
       return render(request, 'events/all_events.html', {'events': events})
@csrf_exempt
def eventsdata(request):
     events =list(Event.objects.values())
     return JsonResponse ( {'events': events},safe=False)
      
