import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_proj.settings')

import django
django.setup()

import random
from first_app.models import Topic,WebPage,AccessRecord
from faker import Faker

fakeGen = Faker()
topics = ["games","social","politics","biz","study"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for ent in range(N):
        top = add_topic()
        fakeName = fakeGen.company()
        fakeUrl = fakeGen.url()
        fakeDate = fakeGen.date()

        webpg = WebPage.objects.get_or_create(topic = top, name = fakeName, url = fakeUrl)[0]
        accRec = AccessRecord.objects.get_or_create(name = webpg, date = fakeDate)[0]

if __name__=="__main__":
    print("populating")
    populate(25)
    print("Complete")
