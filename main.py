import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    passcards = Passcard.objects.all()
    
    for passcard in passcards[:1]:
        print(f'owner_name: {passcard.owner_name}')
        print(f'passcode: {passcard.passcode}')
        print(f'created_at: {passcard.created_at}')
        print(f'is_active: {passcard.is_active}')
