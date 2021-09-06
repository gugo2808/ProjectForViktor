from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponseRedirect
from main.models import Password
from account.form import PasswordForm
from django.shortcuts import render

def check_password(request):
    form = PasswordForm()
    if request.method == "POST":
        form = PasswordForm(request.POST)
        password = request.POST.get("text")
        try:
            password_model = Password.objects.get(pk=1)
        except Exception as e:
            return render(request, "registration/login.html", {'form': form})
        if (password == password_model.text):
            return render(request, "registration/login.html", {'form': form, 'canSee': True})
        form.add_error("text", "Пароль не совпадает.")
        return render(request, "registration/login.html", {'form': form, 'canSee': False})
    return render(request, "registration/login.html", {'form': form, 'canSee': False})
