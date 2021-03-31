from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Lugar


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['nombre', 'texto', 'imagen']

