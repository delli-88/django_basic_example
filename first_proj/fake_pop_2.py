import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_proj.settings')

import django
django.setup()

import random
from first_app.models import Topic,WebPage,AccessRecord
from first_app.models import Branch,StudentGrade,StudentDetails
from faker import Faker
import random

fake = Faker()

branchs = ["CSE","IT","ECE"]
def add_branch():
    b = Branch.objects.get_or_create(branch = random.choice(branchs))[0]
    b.save()
    return b

def populate(N = 5):
    for i in range(N):
        stuBran = add_branch()
        fakeRoll = fake.phone_number()
        fakeName = fake.name()
        fakeGrade = random.choice(["A","B","C","D"])
        if fakeGrade=="A" or fakeGrade=="B" or fakeGrade=="C":
            fakeRes = "PASS"
        else:
            fakeRes = "FAIL"
        stuDet = StudentDetails.objects.get_or_create(branch = stuBran,roll = fakeRoll,name = fakeName)[0]
        stuRes = StudentGrade.objects.get_or_create(roll = stuDet, grade = fakeGrade, result = fakeRes)[0]

if __name__ == '__main__':
    print("populating")
    populate(10)
    print("complete")
