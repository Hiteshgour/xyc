from rest_framework import serializers
from .models import *


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'username', 'email', 'password']
