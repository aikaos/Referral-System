from rest_framework import serializers
from .models import Invites


class InvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invites
        fields = '__all__'



