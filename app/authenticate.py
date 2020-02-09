from django.shortcuts import redirect
from app.models import User

class Authenticate:
    def valid_user(function):
        def wrap(request):

            try:
                User.objects.get(name=request.session['name'])
                return function(request)
            except:
                return redirect("/entry")

            return wrap
