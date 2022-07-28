from rest_framework import serializers
from .models import MailingList, Client


class MailingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
