import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402
import datetime

def get_risk_group(passcard, sick_date):
    patient_visits = Visit.objects.filter(passcard=passcard)
    incubation_date = sick_date - datetime.timedelta(days=7)
    risc_visits = []
    risc_group_visits = []
    for visit in patient_visits:
        if incubation_date <= visit.entered_at.date() <= sick_date:
            risc_visits.append(visit)
    for visit in Visit.objects.all():
        for risc_visit in risc_visits:
            if risc_visit.entered_at < visit.entered_at < risc_visit.leaved_at:
                risc_group_visits.append(visit)
    for visit in risc_group_visits:
        print(visit.passcard, visit.entered_at, sep=' - ')



if __name__ == '__main__':
    sick_date = datetime.date(2021, 8, 1)
    passcard = Passcard.objects.all()[10]
    get_risk_group(passcard, sick_date)