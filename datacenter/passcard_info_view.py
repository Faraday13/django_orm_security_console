from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.services.visit_duration import get_visit_duration, prune_ms

HOUR_IN_SECONDS = 3600

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = get_visit_duration(visit)
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': prune_ms(duration),
                'is_strange': duration.total_seconds() > HOUR_IN_SECONDS
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
