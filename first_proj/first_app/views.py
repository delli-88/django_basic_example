from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app.models import Topic,WebPage,AccessRecord
from first_app.models import StudentGrade,StudentDetails,Branch,LocUser
from first_app import forms
from first_app.forms import NewUserForm,UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    WebPageList = WebPage.objects.order_by('topic')
    dateDict = {"accessRecords":WebPageList}
    studList = StudentGrade.objects.order_by('grade')
    studName = StudentDetails.objects.order_by('name')
    stuDict = {"studs":studList,
                "studNames": studName}
    return render(request,"first_app/index.html",context = stuDict)

def FormPage(request):
    form = forms.FormName()
    if request.method=='POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("Name-"+form.cleaned_data['name'])
            print("Email-"+form.cleaned_data['email'])
            print("Text-"+form.cleaned_data['text'])
    return render(request,"first_app/formPage.html",{"form":form})

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid")
            return index(request)
    return render(request,"first_app/users.html",{"form":form})

def userNames(request):
    userList = LocUser.objects.order_by('firstName')
    userDict = {'users':userList}
    return render(request,"first_app/user_names.html",context = userDict)

def register(request):
    registered = False
    if request.method=="POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,"first_app/register.html",
    {"user_form":user_form,
    "profile_form": profile_form,
    "registered":registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("Welcom to Special Page")

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Not active")
        else:
            print("Wrong")
            return HttpResponse("Inavlid credentials")
    else:
        return render(request,"first_app/login.html",{})
