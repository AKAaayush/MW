from django.shortcuts import render, redirect
from app.models import User
from app.forms import UserForm


# Create your views here.
def index(request):
    form = UserForm()
    return render(request, 'index.html', {'form': form})

def laptos(request):
    return render(request, 'laptos.html')

def about(request):
    return render(request,'about.html')

def apple(request):
    return render (request,'apple.html')

# def dashbord(request):
#     return render(request,'dashbord.html')

# database retrive
def dashbord(request):
    users = User.objects.all()
    return render(request,"dashbord.html",{'users':users})


def create(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        form.save()
        redirect('/')
    form = UserForm()
    return render(request, 'singup.html', {'form': form})

# def subscriber(request):
#     if request.method=="POST":
#         subform=SubscriberForm(request.POST)
#         subform.save()
#         redirect('/')
#         subform = SubscriberForm()
#     return render(request, 'index.html', {'subform': subform})

def edit(request,id):
     user=User.objects.get(user_id=id)
     return render(request,'edit.html',{'user':user})

def update(request,id):
    user =User.objects.get(user_id=id)
    form =UserForm(request.POST,instance=user)
    form.save()
    return redirect('/')

def delete(request,id):
    user=User.objects.get(user_id=id)
    user.delete()
    return redirect('/')



