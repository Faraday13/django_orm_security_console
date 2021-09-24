from datacenter.passcard_info_view import HOUR_IN_SECONDS
from datacenter.services.visit_duration import get_visit_duration, prune_ms
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration = get_visit_duration(visit)
        non_closed_visits.append({
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': prune_ms(duration),
                'is_strange': duration.total_seconds() > HOUR_IN_SECONDS
            })
        
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
