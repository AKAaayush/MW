from django.contrib import messages
from django.shortcuts import redirect
from app.models import User
from django.db.models import Q


class Authenticate:

    def valid_login(function):
        def login(request):
            try:

                User.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))

                return function(request)

            except:
                messages.warning(request, "Please Enter valid email or password.")
            return redirect("/login")

        return login
