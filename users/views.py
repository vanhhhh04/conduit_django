from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import HttpResponse
# Create your views here.
from .forms import UserForm 
from .authentication import encode_jwt,decode_jwt
from rest_framework.authtoken.models import Token

import json 



@csrf_exempt
@require_http_methods(['POST'])
def user_register(request):
    if request.method == "POST":
        try :
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        data = data.get('user',{})
        form = UserForm(data)
        payload = f"{data.get("username")}"
        a = encode_jwt(payload=payload)
        b = decode_jwt(a)
        print(a)
        print(b)
        if form.is_valid():
            print("Authentication successfully")
            response_data = {
                "id": 1,
                "username": "aaa",
                "email": "a@gmail.com"
            }
            return JsonResponse({"user": response_data}, status=200)
        else:
            return JsonResponse({"erros": form.errors}, status=400)
        

@csrf_exempt
@require_http_methods(['POST'])
def user_login(request):
    if request.method == "POST":
        data = request.POST
        print(UserForm())
        form = UserForm(data)
        print("[AAAA]")
        print(form)
        if form.is_valid():
            print("Authentication successfully")
        else:
            print("Not success")
        return HttpResponse("AAAA")


