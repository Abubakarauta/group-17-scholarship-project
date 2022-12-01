from django.shortcuts import render,redirect 
from .forms import ProfileForm, applicant_bio,applicant_NEXT_OF_KIN,applicant_CURRENT_ACADEMIC_LEVEL,applicant_upload_certificates,applicant_bio_edit
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .models import Bio_data, Profile
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Dashboard(request):
    return render(request, 'portfolio.html')

def FAQ(request):
    return render(request, 'pricing.html')

def bio(request):
    bio_form = applicant_bio()
    if request.method=='POST':
        bio_form = applicant_bio(request.POST)
        if bio_form.is_valid():
            bio_form.save()
            return redirect('next_of_kin')
    context={
        'bio_form':bio_form
    }
    return render(request, 'bio.html', context)

def bio_edit(request,id):
    instance = Bio_data.objects.get(id=id)
    bio_form=applicant_bio_edit(instance=instance)
    if request.method=='POST':
        bio_form=applicant_bio_edit(request.POST,instance=instance)
        if bio_form.is_valid():
            bio_form.save()
            return redirect('bio')
    context={
        'bio_form':bio_form,
        'instance':instance
    }
    return render(request, 'bio-edit.html',context)


def NEXT_OF_KIN(request):
    nok_form= applicant_NEXT_OF_KIN()
    if request.method=='POST':
        nok_form=applicant_NEXT_OF_KIN(request.POST)
        if nok_form.is_valid():
            nok_form.save()
            return redirect('current_acdemic_level')
    context={
        'nok_form':nok_form
    }
    return render(request, 'next-of-kin.html',context)

def CURRENT_ACADEMIC_LEVEL(request):
    cal_form=applicant_CURRENT_ACADEMIC_LEVEL()
    if request.method=='POST':
        cal_form=applicant_CURRENT_ACADEMIC_LEVEL(request.POST)
        if cal_form.is_valid():
            cal_form.save()
            return redirect('upload_certificates')
    context={
        'cal_form':cal_form
    }
    return render(request, 'current-academic-level.html',context)

def UPLOAD_CERTIFICATES(request):
    uc_form=applicant_upload_certificates()
    if request.method=='POST':
        uc_form=applicant_upload_certificates(request.POST)
        if uc_form.is_valid():
            uc_form.save()
            return redirect('Dashboard')

    context={
        'uc_form':uc_form
    }
    return render(request,'upload-certificates.html',context)

def Register(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        last_name=request.POST.get('last_name')
        first_name=request.POST.get('first_name')
        phone_number=request.POST.get('phone_number')
        confirm_password=request.POST.get('confirm_password') 


        if password==confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'username exists')
                return redirect('register')
            else:
                #user = User.objects.create_user(**request.POST) # same as theone below
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'account successfully created')
                team = ProfileForm(data={ 'user' : user })
                if team.is_valid(): team.save()
                return redirect('login')
        else:
            messages.error(request,'password not the same')
        return redirect('register')
    else:    
        return render(request,'register.html')

def Login_views(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is None:
            context = { 'error' : 'Invalid username or password.' }
            return render(request ,'login.html', context)
        login(request,user)
        return redirect('Dashboard')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def members_view(request):
    context = { 'members' : Profile.objects.filter(is_team=True) }
    return render(request, 'members.html', context)