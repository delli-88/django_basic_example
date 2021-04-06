from django.contrib import admin
from first_app.models import Topic,WebPage,AccessRecord,UserProfileInfo
from first_app.models import Branch,StudentDetails,StudentGrade,LocUser
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(Branch)
admin.site.register(StudentDetails)
admin.site.register(StudentGrade)
admin.site.register(LocUser)
admin.site.register(UserProfileInfo)
