from django.forms import *
from main.models import Password

class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = '__all__'
