from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.http import HttpResponse, JsonResponse
from app.authenticate import Authenticate
from app.models import User, Admin
from app.forms import UserForm, AdminForm
from django.contrib.auth.models import auth


# Create your views here.
def index(request):
    form = UserForm()
    return render(request, 'entry.html', {'form': form})


def laptos(request):
    return render(request, 'laptos.html')


def about(request):
    return render(request, 'about.html')


def apple(request):
    return render(request, 'apple.html')


# def dashbord(request):
#     return render(request,'dashbord.html')

# database retrive

@Authenticate.valid_login
def userdetail(request):
    users = User.objects.all()
    return render(request, "entry.html", {'users': users})


def admintable(request):
    adminuser = Admin.objects.all()
    return render(request, "admintable.html", {'adminusers': adminuser})


def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
        redirect('/')
    form = UserForm()
    return render(request, 'singup.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def entry(request):
    request.session['name'] = request.POST['name']
    request.session['password'] = request.POST['password']
    redirect('/entry')
    return render(request, 'entry.html')


def loginvalid(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/userdetail')


# def subscriber(request):
#     if request.method=="POST":
#         subform=SubscriberForm(request.POST)
#         subform.save()
#         redirect('/')
#         subform = SubscriberForm()
#     return render(request, 'index.html', {'subform': subform})

def edit(request, id):
    user = User.objects.get(user_id=id)
    return render(request, 'edit.html', {'user': user})


def update(request, id):
    user = User.objects.get(user_id=id)
    form = UserForm(request.POST, instance=user)
    form.save()
    return redirect('/')


def delete(request, id):
    user = User.objects.get(user_id=id)
    user.delete()
    return redirect('/userdetail')


def admindelete(request, adminid):
    adminuser = Admin.objects.get(id=adminid)
    adminuser.delete()
    return redirect('/admintable')


def create1(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        form.save()
        redirect('/')
    form = AdminForm()
    return render(request, 'create1.html', {'form': form})


def edit1(request, adminid):
    user = Admin.objects.get(id=adminid)
    return render(request, 'edit1.html', {'user': user})


def update1(request, adminid):
    admin = Admin.objects.get(id=adminid)
    form = AdminForm(request.POST, instance=admin)
    form.save()
    return redirect('/')
