from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
# Create your views here.
from .forms import UserForm 
from .models import User 
from .authentication import encode_jwt,decode_jwt
# from rest_framework.authtoken.models import Token

import json 
import time 


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

        if form.is_valid():
            form_data = form.cleaned_data 
            email = form_data.get('email')
            username = form_data.get('username')
            password = form_data.get('password')          

            user = User.objects.create(
                username = username,
                email = email,
                password = make_password(password)
            )
            
            payload = {
                'user_ud': user.id,
                'username': user.username,
                'exp': int(time.time()) + 3600
            }
            
            token = encode_jwt(payload)
            print(token)
            response_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'token': token 
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


