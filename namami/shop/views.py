from django.shortcuts import render, redirect
from .serializers import RegisterSerializers
from rest_framework import viewsets
from rest_framework import permissions
from .models import *


# Create your views here.
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers
    permissions_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


def register(request):
    if request.method == 'GET':
        if request.GET.get('output') == None:
            output = ""
        else:
            output = request.GET.get('output')

        return render(request, "login.html", {'output': output})
    else:
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        Data = Register(name=name, username=username, email=email, password=password)
        Data.save()
        myurl = 'rs/?output=Register successfully'
        return redirect('rs/')



