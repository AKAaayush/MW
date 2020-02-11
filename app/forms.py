from django import forms
from app.models import User, Admin


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"


class loginform(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class adminloginform(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"


class adminloginform(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
