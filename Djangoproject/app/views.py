import random

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .form import *
# Create your views here.


def home(request):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    else:
        return redirect('/user/')




def otpsend(request, email):
    if request.session.get('id', 'otp_msg') == 'None':
        del request.session['otp_msg']


    try:
        d = UserRecord.objects.filter(Email__exact=email)
        if len(d) != 0:
            res = 0
        rand = random.randint(100000, 999999)
        message = f"your otp is {rand}"
        subject = "MemeStream Email Verification"
        send_mail(subject, message, 'helpdeskricla@gmail.com', [email])
        request.session['otp_msg'] = rand
        request.session.set_expiry(60)
        res = 1
    except Exception as err:
        res = str(err)
    return JsonResponse({'response': res })


def otpvalidation(request, otp):
    try:
        email_otp = request.session.get('otp_msg')
        if str(otp) == str(email_otp):
            res = 1
        else:
            res = 0
    except Exception as err:
        res = 0
    return JsonResponse({'response': res})


def signup(request):
    msg = ""
    if request.method == 'POST':
        form = UserRecord()
        form.Name = request.POST['username']
        form.Gender = request.POST['gender']
        form.Email = request.POST['email_id']
        form.Password = request.POST['paasword']
        form.save()
        msg = "User added successfully"
    return render(request, 'emailverification.html', {'msg': msg})


def userpage(request):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    id = request.session.get('id')
    profile = UserRecord.objects.get(id=id)
    data = Post.objects.all().order_by('-id')
    return render(request, 'userpage.html', {'profile':profile, 'data':data})


def userprofile(request):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    id = request.session.get('id')
    profile = UserRecord.objects.get(id=id)
    data = Post.objects.filter(User_Name_id=id)
    return render(request, 'userprofile.html', {'profile': profile, 'data': data})


def login(request):
    msg = ""
    if request.method == 'POST':
        users = UserRecord.objects.filter(Email__exact=request.POST['email_id']).filter(Password__exact=request.POST['paassword'])
        if len(users) != 0:
            request.session['id'] = users[0].id
            return redirect('/')
        else:
            msg = "User id or password are invalid!"
    return render(request, 'base.html', {'msg': msg})


def logout(request):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    del request.session['id']
    return redirect('/login/')


def addPost(request):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    msg = ""
    data = {
        'User_Name':request.session.get('id')
    }
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            msg = "Uploaded successfully"
            return redirect('/user/')
        else:
            msg = "Failed!"
    form = PostForm(initial=data)
    id = request.session.get('id')
    profile = UserRecord.objects.get(id=id)
    return render(request, 'addpost.html', {'form': form, 'msg': msg, 'profile':profile})


def deletePost(request, id):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    data = Post.objects.get(id=id)
    data.delete()
    return redirect('/profile/')


def updatePost(request, id):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    data = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None, instance=data )
        form.save()
        return redirect('/profile/')
    form = PostForm(instance=data)
    id = request.session.get('id')
    profile = UserRecord.objects.get(id=id)
    return render(request, 'addpost.html', {'form': form, 'profile':profile})


def updateProfile(request, id):
    if request.session.get('id', 'None') == 'None':
        return redirect('/login/')
    data = UserRecord.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES or None, instance=data)
        form.save()
        return redirect('/profile/')
    form = UserForm(instance=data)
    id = request.session.get('id')
    profile = UserRecord.objects.get(id=id)
    return render(request, 'updateprofile.html', {'form':form, 'profile':profile})