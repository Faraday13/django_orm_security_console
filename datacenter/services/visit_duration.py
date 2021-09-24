from django.utils.timezone import localtime

def get_visit_duration(visit, str_value=True):
    if visit.leaved_at is None:
        return localtime() - visit.entered_at
    return visit.leaved_at - visit.entered_at

def prune_ms(time):
    return str(time).split('.')[0]