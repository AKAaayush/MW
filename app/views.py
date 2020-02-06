from django.shortcuts import render,redirect
from app.models import User
from app.forms import UserForm


# Create your views here.
def index(request):

    return render(request, 'index.html')

def laptos(request):
    return render(request,'laptos.html')

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

def user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        form.save()
        redirect('/')
    form = UserForm()
    return render(request, 'index.html', {'form': form})




