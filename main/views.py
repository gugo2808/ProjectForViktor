from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required("canSee")
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to="/login")
    return render(request, "anytext.html", {})
