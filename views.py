from django.shortcuts import render
from .models import Event, Organization

def event_list(request):
    query = request.GET.get('q')
    org_id = request.GET.get('organization')  # organizasyon ID'si al

    events = Event.objects.all()

    if query:
        events = events.filter(title__icontains=query)

    if org_id:
        events = events.filter(organizer_id=org_id)

    events = events.order_by('date')
    organizations = Organization.objects.all()  # dropdown listesi için

    return render(request, 'event_list.html', {
        'events': events,
        'query': query,
        'organizations': organizations,
        'selected_org': int(org_id) if org_id else None
    })
