from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="/login")
    return render(request, "anytext.html", {})
