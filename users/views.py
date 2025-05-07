from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here.

@require_http_methods(["POST"])
def user_login(request):
    return HttpResponse("AAAA")

