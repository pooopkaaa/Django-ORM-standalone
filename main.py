import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    passcards = Passcard.objects.all()
    active_passcards = []

    for passcard in passcards:
        if passcard.is_active:
            active_passcards.append(passcard)

    print('Всего пропусков:', Passcard.objects.count())
    print('Активных пропусков', len(active_passcards))
