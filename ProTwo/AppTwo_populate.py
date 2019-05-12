import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()


from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fakeNameArray = fakegen.name().split(" ")
        firstName = fakeNameArray[0]
        lastName = fakeNameArray[1]
        Ema = firstName + lastName + '@gmail.com'
        user = User.objects.get_or_create(first_name = firstName, last_name = lastName, Email = Ema)[0]


if __name__ == '__main__':
    print('populating...')
    populate(30)
    print('populate complete')
